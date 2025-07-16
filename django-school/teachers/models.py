from django.db import models
from django.urls import reverse

# Create your models here.
class Teacher(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    teacher_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Teacher Name')
    teacher_email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Teacher Email')
    teacher_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Teacher Phone')
    teacher_address = models.CharField(max_length=100, null=True, blank=True, verbose_name='Teacher Address')
    teacher_gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Teacher Gender')
    academic_level = models.CharField(max_length=100, null=True, blank=True, verbose_name='Academic Level')
    teacher_date_of_birth = models.DateField(null=True, blank=True, verbose_name='Teacher Date of Birth')
    teacher_date_of_joining = models.DateField(null=True, blank=True, verbose_name='Teacher Date of Joining')
    teacher_date_of_leaving = models.DateField(null=True, blank=True, verbose_name='Teacher Date of Leaving')

    def __str__(self):
        return self.teacher_name
    
    def get_absolute_url(self):
        return reverse('teacher.detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['teacher_name']
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        indexes = [models.Index(fields=['teacher_name'])]
        unique_together = ['teacher_name', 'teacher_email', 'teacher_phone', 'teacher_address', 'teacher_gender', 'teacher_date_of_birth', 'teacher_date_of_joining', 'teacher_date_of_leaving']
        db_table = 'teachers'