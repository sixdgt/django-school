from django.contrib import admin
from school.models import School, AcademicYear

# Register your models here.
admin.site.register(School)
admin.site.register(AcademicYear)