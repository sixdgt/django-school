from django.db import models
from teachers.models import Teacher
from subjects.models import Subject
from classdetail.models import ClassDetail
from school.models import AcademicYear
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Material(models.Model):
    MATERIAL_CATEGORY = [
        ('SLIDE', 'Chapter Slide'),
        ('TEXT_BOOK', 'A text book'),
        ('REFERENCE_BOOK', 'A reference book'),
        ('OLD_QUESTION', 'Previous board exam question'),
        ('AUDIO_BOOK', 'An audio book')
    ]
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Material Title')
    category = models.CharField(max_length=30, choices=MATERIAL_CATEGORY, null=False, blank=False, verbose_name='Category')
    description = models.CharField(max_length=255, default='', null=False, blank=False, verbose_name='Material Description')
    material_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Material Subject')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name='Academic Year')
    class_name = models.ForeignKey(ClassDetail, on_delete=models.CASCADE, verbose_name='Class Name')
    material_file = models.FileField(upload_to='material/', null=False, blank=False, verbose_name='Select file')
    upload_date = models.DateTimeField(default=datetime.now, verbose_name='Upload Date')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Uploaded By')

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materials'
        ordering = ['-title']

    def get_category_display(self):
        return dict(self.MATERIAL_CATEGORY)[self.category]

    def get_absolute_url(self):
        return reverse('material.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title