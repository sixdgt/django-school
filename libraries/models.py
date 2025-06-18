from django.db import models
from django.urls import reverse

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Name')
    book_author = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Author')
    book_publisher = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Publisher')
    book_publication_date = models.DateField(null=True, blank=True, verbose_name='Book Publication Date')
    book_isbn = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book ISBN')
    book_category = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Category')
    book_quantity = models.IntegerField(null=True, blank=True, verbose_name='Book Quantity')
    book_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Book Price')
    book_description = models.TextField(max_length=100, null=True, blank=True, verbose_name='Book Description')
    book_status = models.CharField(max_length=100, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost')])
    book_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Location')
    book_shelf = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Shelf')
    book_row = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Row')
    book_column = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Column')
    book_level = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Level')
    book_section = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Section')
    book_sub_section = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Sub Section')
    book_rack_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Rack Number')
    book_row_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Row Number')
    book_column_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Column Number')
    book_level_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Book Level Number')

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('library.detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['book_name']
        verbose_name = 'library'
        verbose_name_plural = 'libraries'
        indexes = [models.Index(fields=['book_name'])]
        db_table = 'library'
