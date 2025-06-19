from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from school.models import AcademicYear
from classdetail.models import ClassDetail
from subjects.models import Subject
from students.models import Student


# Create your models here.
class Term(models.Model):
    term_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Term Name')
    term_description = models.CharField(max_length=100, null=True, blank=True, verbose_name='Term Description')
    term_status = models.CharField(max_length=100, choices=[('active', 'Active'), ('inactive', 'Inactive')], null=True, blank=True, verbose_name='Term Status')

    def __str__(self):
        return self.term_name

    def get_absolute_url(self):
        return reverse('term.detail', args=[str(self.id)])

class Exam(models.Model):
    EXAM_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    exam_term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Term')
    exam_date = models.DateField(null=True, blank=True, verbose_name='Exam Date')
    exam_time = models.TimeField(null=True, blank=True, verbose_name='Exam Time')
    exam_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Subject')
    exam_class = models.ForeignKey(ClassDetail, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Class')
    exam_level = models.CharField(max_length=100, null=True, blank=True, verbose_name='Exam Level')
    exam_status = models.CharField(max_length=100, choices=EXAM_STATUS_CHOICES, null=True, blank=True, verbose_name='Exam Status')
    exam_academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Academic Year')

    def __str__(self):
        return self.exam_term

    def get_absolute_url(self):
        return reverse('exam.detail', args=[str(self.id)])

    class Meta:
        ordering = ['exam_term']
        verbose_name = 'exam'
        verbose_name_plural = 'exams'
        indexes = [models.Index(fields=['exam_term'])]
        unique_together = ['exam_term', 'exam_date', 'exam_time', 'exam_subject', 'exam_class', 'exam_level', 'exam_status', 'exam_academic_year']
        db_table = 'exams'

class ExamSubject(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam')
    exam_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam Subject')
    full_marks = models.FloatField(null=True, blank=True, verbose_name='Full Marks')
    pass_marks = models.FloatField(null=True, blank=True, verbose_name='Pass Marks')
    theory_marks = models.FloatField(null=True, blank=True, verbose_name='Theory Marks')
    practical_marks = models.FloatField(null=True, blank=True, verbose_name='Practical Marks')
    credit_hours = models.FloatField(null=True, blank=True, verbose_name='Credit Hours')

    def __str__(self):
        return self.exam_subject.subject_name

    def get_absolute_url(self):
        return reverse('exam_subject.detail', args=[str(self.id)])

class ExamLedger(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    EXAM_LEDGER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    exam = models.ForeignKey(ExamSubject, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Exam')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Student')
    obtained_marks = models.FloatField(null=True, blank=True, verbose_name='Obtained Marks')
    grade = models.CharField(max_length=25, choices=GRADE_CHOICES, null=True, blank=True, verbose_name='Grade')
    grade_point = models.FloatField(null=True, blank=True, verbose_name='Grade Point')
    weighted_grade = models.FloatField(null=True, blank=True, verbose_name='Weighted Grade')
    remarks = models.TextField(null=True, blank=True, verbose_name='Remarks')
    exam_ledger_status = models.CharField(max_length=100, choices=EXAM_LEDGER_STATUS_CHOICES, null=True, blank=True, verbose_name='Exam Ledger Status')

    def __str__(self):
        return self.student.student_name

    def get_absolute_url(self):
        return reverse('exam_ledger.detail', args=[str(self.id)])

    class Meta:
        ordering = ['student']
        verbose_name = 'exam_ledger'
        verbose_name_plural = 'exam_ledgers'
        indexes = [models.Index(fields=['student'])]
        unique_together = ['exam', 'student']
        db_table = 'exam_ledgers'
