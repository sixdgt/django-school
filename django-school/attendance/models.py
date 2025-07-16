from django.db import models
from django.urls import reverse

# Create your models here.
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('early_out', 'Early Out'),
    ]
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Student')
    date = models.DateField(null=True, blank=True, verbose_name='Date')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True, blank=True, verbose_name='Status')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Subject')
    class_name = models.ForeignKey('classdetail.ClassDetail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Class Name')
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Teacher')

    def __str__(self):
        return self.student.student_name
    
    def get_absolute_url(self):
        return reverse('attendance.detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['student']
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'
        indexes = [models.Index(fields=['student'])]
        unique_together = ['student', 'date', 'status', 'subject', 'class_name', 'teacher']
        db_table = 'attendances'