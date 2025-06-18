from django.db import models
from django.urls import reverse

# Create your models here.
class Result(models.Model):
    result_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Result Name')
    result_date = models.DateField(null=True, blank=True, verbose_name='Result Date')
    result_class = models.ForeignKey('classdetail.ClassDetail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Result Class')
    result_student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Result Student')
    result_subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Result Subject')
    result_marks = models.IntegerField(null=True, blank=True, verbose_name='Result Marks')
    result_status = models.CharField(max_length=100, choices=[('pass', 'Pass'), ('fail', 'Fail')], null=True, blank=True, verbose_name='Result Status')
    result_grade = models.CharField(max_length=100, null=True, blank=True, verbose_name='Result Grade')
    result_remarks = models.TextField(max_length=100, null=True, blank=True, verbose_name='Result Remarks')
    result_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Result Percentage')
    result_rank = models.IntegerField(null=True, blank=True, verbose_name='Result Rank')

    def __str__(self):
        return self.result_name
    
    def get_absolute_url(self):
        return reverse("result.detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['result_name']
        verbose_name = 'result'
        verbose_name_plural = 'results'
        indexes = [models.Index(fields=['result_name'])]
        unique_together = ['result_name', 'result_date', 'result_class', 'result_student', 'result_subject']
        db_table = 'results'
