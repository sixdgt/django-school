from django.db import models
from django.urls import reverse

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
    established_date = models.DateField(verbose_name='School Established Date')

    class Meta:
        indexes = [models.Index(fields=['full_name'])]
        ordering = ['-full_name']
        verbose_name = 'school'
        verbose_name_plural = 'school'
        
    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("school_detail", kwargs={"pk": self.pk})
    
class AcademicYear(models.Model):
    academic_year_name = models.CharField(max_length=100, verbose_name='Academic Year Name')
    academic_year_start_date = models.DateField(verbose_name='Academic Year Start Date')
    academic_year_end_date = models.DateField(verbose_name='Academic Year End Date')
    academic_year_status = models.CharField(max_length=100, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', verbose_name='Academic Year Status')
    
    class Meta:
        indexes = [models.Index(fields=['academic_year_name'])]
        ordering = ['-academic_year_name']
        verbose_name = 'academic year'
        verbose_name_plural = 'academic years'
        unique_together = ['academic_year_name', 'academic_year_start_date', 'academic_year_end_date']
        db_table = 'academic_years'

    def __str__(self):
        return self.academic_year_name
    
    def get_absolute_url(self):
        return reverse("academic_year_detail", kwargs={"pk": self.pk})