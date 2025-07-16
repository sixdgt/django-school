from django.db import models
from django.urls import reverse

# Create your models here.
class ClassDetail(models.Model):
    CLASS_TYPE_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('higher_secondary', 'Higher Secondary'),
    ]
    CLASS_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    class_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Class Name')
    class_teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Class Teacher')
    class_type = models.CharField(max_length=100, choices=CLASS_TYPE_CHOICES, null=True, blank=True, verbose_name='Class Type')
    class_status = models.CharField(max_length=100, choices=CLASS_STATUS_CHOICES, null=True, blank=True, verbose_name='Class Status')
    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse('classdetail.detail', args=[str(self.id)])

    class Meta:
        ordering = ['class_name']
        verbose_name = 'classdetail'
        verbose_name_plural = 'classdetails'
        indexes = [models.Index(fields=['class_name'])]
        unique_together = ['class_name', 'class_teacher', 'class_type', 'class_status']
        db_table = 'class_details'

