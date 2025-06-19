from django.db import models
from django.urls import reverse

# Create your models here.
class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = [
        ('theory', 'Theory'),
        ('practical', 'Practical'),
    ]
    SUBJECT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    subject_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Subject Name')
    subject_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='Subject Code')
    subject_description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Subject Description')
    class_name = models.ForeignKey('classdetail.ClassDetail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Class Name')
    subject_teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Subject Teacher')
    subject_type = models.CharField(max_length=100, choices=SUBJECT_TYPE_CHOICES, null=True, blank=True, verbose_name='Subject Type')
    credit_hours = models.FloatField(null=True, blank=True, verbose_name='Credit Hours')
    subject_status = models.CharField(max_length=100, choices=SUBJECT_STATUS_CHOICES, null=True, blank=True, verbose_name='Subject Status')

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('subject.detail', args=[str(self.id)])

    class Meta:
        ordering = ['subject_name']
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        indexes = [models.Index(fields=['subject_name'])]
        unique_together = ['subject_name', 'subject_code', 'subject_description', 'class_name', 'subject_teacher', 'subject_type', 'credit_hours', 'subject_status']
        db_table = 'subjects'