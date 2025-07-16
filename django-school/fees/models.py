from django.db import models
from django.urls import reverse

# Create your models here.
class Fee(models.Model):
    fee_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Fee Name')
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Fee Amount')
    fee_date = models.DateField(null=True, blank=True, verbose_name='Fee Date')
    fee_class = models.ForeignKey('classdetail.ClassDetail', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Fee Class')
    fee_student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Fee Student')
    fee_status = models.CharField(max_length=100, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], null=True, blank=True, verbose_name='Fee Status')
    fee_description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Fee Description')
    fee_payment_method = models.CharField(max_length=100, choices=[('cash', 'Cash'), ('bank_transfer', 'Bank Transfer'), ('cheque', 'Cheque')], null=True, blank=True, verbose_name='Fee Payment Method')
    fee_payment_date = models.DateField(null=True, blank=True, verbose_name='Fee Payment Date')
    fee_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Fee Payment Amount')
    fee_payment_status = models.CharField(max_length=100, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], null=True, blank=True, verbose_name='Fee Payment Status')
    fee_payment_description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Fee Payment Description')

    def __str__(self):
        return self.fee_name

    def get_absolute_url(self):
        return reverse('fee.detail', args=[str(self.id)])

    class Meta:
        ordering = ['fee_name']
        verbose_name = 'fee'
        verbose_name_plural = 'fees'
        indexes = [models.Index(fields=['fee_name'])]
        db_table = 'fees'