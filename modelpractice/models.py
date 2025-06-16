from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import date
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
import uuid

# Create your models here.

class School(models.Model):
    SCHOOL_TYPE = (
        ('PUBLIC', 'A Public School'),
        ('PRIVATE', 'A Private School'),
    )
    full_name = models.CharField(max_length=100, verbose_name='School Full Name')
    school_type = models.CharField(max_length=10, choices=SCHOOL_TYPE, default='PUBLIC', verbose_name='School Type')
    address = models.CharField(max_length=100, verbose_name='School Address')
    city = models.CharField(max_length=100, verbose_name='School City')
    state = models.CharField(max_length=100, verbose_name='School State')
    zip_code = models.CharField(max_length=10, verbose_name='School Zip Code')
    phone = models.CharField(max_length=10, verbose_name='School Phone')
    website = models.URLField(max_length=100, verbose_name='School Website')
    principal = models.CharField(max_length=100, verbose_name='School Principal Name')

    class Meta:
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['-full_name']
        verbose_name = 'school'
        verbose_name_plural = 'school'
        
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("school_detail", kwargs={"pk": self.pk})
    
class Student(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )

    # Phone number validator (10 digits)
    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message='Phone number must be exactly 10 digits.'
    )

    # Zip code validator (5 digits)
    zip_code_validator = RegexValidator(
        regex=r'^\d{5}$',
        message='Zip code must be exactly 5 digits.'
    )

    registration_code = models.CharField(max_length=10, unique=True, editable=False)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone = models.CharField(max_length=10, verbose_name='Phone', validators=[phone_validator])
    address = models.CharField(max_length=100, verbose_name='Address')
    city = models.CharField(max_length=100, verbose_name='City')
    state = models.CharField(max_length=100, verbose_name='State')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code', validators=[zip_code_validator])
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='MALE', verbose_name='Gender')
    parent_name = models.CharField(max_length=100, verbose_name='Parent Name')
    parent_phone = models.CharField(max_length=10, verbose_name='Parent Phone', validators=[phone_validator])
    parent_email = models.EmailField(max_length=100, verbose_name='Parent Email', validators=[EmailValidator()])
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', related_query_name='person')
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
            models.Index(fields=['registration_code']),
            models.Index(fields=['date_of_birth']),
        ]
        ordering = ['-first_name']
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def generate_registration_code(self):
        """Generate a unique registration code in format: YYYY-XXXXX"""
        year = date.today().year
        # Get the last registration code for this year
        last_code = Student.objects.filter(
            registration_code__startswith=str(year)
        ).order_by('-registration_code').first()
        
        if last_code:
            # Extract the number part and increment
            last_number = int(last_code.registration_code.split('-')[1])
            new_number = last_number + 1
        else:
            # First code for this year
            new_number = 1
        
        # Format: YYYY-XXXXX (padded with zeros)
        return f"{year}-{new_number:05d}"

    def generate_qr_code(self):
        """Generate QR code for the student's registration code"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.registration_code)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to BytesIO
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        
        # Save to model
        filename = f'qr_code_{self.registration_code}.png'
        self.qr_code.save(filename, File(buffer), save=False)

    def save(self, *args, **kwargs):
        if not self.registration_code:
            self.registration_code = self.generate_registration_code()
        if not self.qr_code:
            self.generate_qr_code()
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        # Validate date of birth (student must be at least 5 years old)
        if self.date_of_birth:
            age = (date.today() - self.date_of_birth).days / 365.25
            if age < 5:
                raise ValidationError({'date_of_birth': 'Student must be at least 5 years old.'})
            if age > 25:
                raise ValidationError({'date_of_birth': 'Student age seems incorrect. Please verify the date of birth.'})

        # Validate that parent email is not the same as student's school email domain
        if self.parent_email and self.school:
            school_domain = self.school.website.split('@')[-1] if '@' in self.school.website else None
            parent_domain = self.parent_email.split('@')[-1]
            if school_domain and parent_domain == school_domain:
                raise ValidationError({
                    'parent_email': 'Parent email cannot use the school email domain.'
                })

        # Validate that phone numbers are different
        if self.phone == self.parent_phone:
            raise ValidationError({
                'parent_phone': 'Parent phone number must be different from student phone number.'
            })