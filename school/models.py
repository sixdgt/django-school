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