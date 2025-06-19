from django.db import models
from teachers.models import Teacher
from subjects.models import Subject
from classdetail.models import ClassDetail
from school.models import AcademicYear
from django.urls import reverse

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Title')
    start_date = models.DateField(null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(blank=False, null=False, verbose_name='End Date')
    question_file = models.FileField(upload_to='assignments/questions/', null=True, blank=True, verbose_name='Select Assignment File')
    question = models.TextField(null=True, blank=True, verbose_name='Assignment Question')
    remark = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Details')
    full_mark = models.FloatField(blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Uploaded By')
    assignment_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Assignment Subject')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name='Academic Year')
    class_name = models.ForeignKey(ClassDetail, on_delete=models.CASCADE, verbose_name='Class Name')
    
    class Meta:
        verbose_name = 'assignment'
        verbose_name_plural = 'assignments'
        ordering = ['-title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('assignment.detail', kwargs={'pk': self.pk})