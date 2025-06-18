from django.db import models
from django.urls import reverse

# Create your models here.
class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('first_term', 'First Term'),
        ('second_term', 'Second Term'),
        ('third_term', 'Third Term'),
        ('final_term', 'Final Term'),
    ]
    EXAM_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    exam_term = models.CharField(max_length=100, choices=EXAM_TYPE_CHOICES, null=True, blank=True, verbose_name='Exam Term')
    exam_date = models.DateField(null=True, blank=True, verbose_name='Exam Date')
    exam_time = models.TimeField(null=True, blank=True, verbose_name='Exam Time')
    exam_subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Subject')
    exam_class = models.ForeignKey('classdetail.ClassDetail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Class')
    full_marks = models.IntegerField(null=True, blank=True, verbose_name='Full Marks')
    pass_marks = models.IntegerField(null=True, blank=True, verbose_name='Pass Marks')
    theory_marks = models.IntegerField(null=True, blank=True, verbose_name='Theory Marks')
    practical_marks = models.IntegerField(null=True, blank=True, verbose_name='Practical Marks')
    credit_hours = models.IntegerField(null=True, blank=True, verbose_name='Credit Hours')
    exam_level = models.CharField(max_length=100, null=True, blank=True, verbose_name='Exam Level')
    exam_status = models.CharField(max_length=100, choices=EXAM_STATUS_CHOICES, null=True, blank=True, verbose_name='Exam Status')

    def __str__(self):
        return self.exam_term

    def get_absolute_url(self):
        return reverse('exam.detail', args=[str(self.id)])

    class Meta:
        ordering = ['exam_term']
        verbose_name = 'exam'
        verbose_name_plural = 'exams'
        indexes = [models.Index(fields=['exam_term'])]
        unique_together = ['exam_term', 'exam_date', 'exam_time', 'exam_subject', 'exam_class', 'full_marks', 'pass_marks', 'theory_marks', 'practical_marks', 'credit_hours', 'exam_level', 'exam_status']
        db_table = 'exams'