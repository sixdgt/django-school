from django.shortcuts import render
from modelpractice.models import Student, School
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.db.models import Q
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Image
from django.conf import settings
import os

# Create your views here.
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_index.html'
    context_object_name = 'students'
    ordering = ['-school']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            # Try to parse as date first
            try:
                from datetime import datetime
                search_date = datetime.strptime(search_query, '%Y-%m-%d').date()
                queryset = queryset.filter(date_of_birth=search_date)
            except ValueError:
                # If not a date, search in other fields
                queryset = queryset.filter(
                    Q(registration_code__icontains=search_query) |
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query) |
                    Q(first_name__icontains=search_query.split()[0]) & Q(last_name__icontains=search_query.split()[-1])
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = [
        'first_name', 'last_name', 'phone', 'address', 'city', 'state', 
        'zip_code', 'date_of_birth', 'gender', 'parent_name', 
        'parent_phone', 'parent_email', 'school'
    ]
    success_url = reverse_lazy('student.index')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, f'Student {form.instance.get_full_name()} has been successfully created.')
            return response
        except ValidationError as e:
            for field, errors in e.message_dict.items():
                form.add_error(field, ErrorList(errors))
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = [
        'first_name', 'last_name', 'phone', 'address', 'city', 'state', 
        'zip_code', 'date_of_birth', 'gender', 'parent_name', 
        'parent_phone', 'parent_email', 'school'
    ]
    success_url = reverse_lazy('student.index')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, f'Student {form.instance.get_full_name()} has been successfully updated.')
            return response
        except ValidationError as e:
            for field, errors in e.message_dict.items():
                form.add_error(field, ErrorList(errors))
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student.index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # You can add additional security checks here if needed
        # For example, checking if the user has permission to delete this student
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Student {self.get_object().get_full_name()} has been successfully deleted.')
        return super().delete(request, *args, **kwargs)

class StudentIDCardView(LoginRequiredMixin, TemplateView):
    template_name = 'student_id_card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(pk=kwargs['pk'])
        context['student'] = student
        return context

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['pk'])
        
        # Create the PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="student_id_{student.registration_code}.pdf"'
        
        # Create the PDF object
        p = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        # Add school logo if exists
        if student.school.website:  # You might want to add a logo field to School model
            p.drawString(50, height - 50, f"School: {student.school.full_name}")

        # Add student information
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, height - 100, "STUDENT IDENTIFICATION CARD")
        
        p.setFont("Helvetica", 12)
        p.drawString(50, height - 130, f"Registration Code: {student.registration_code}")
        p.drawString(50, height - 150, f"Name: {student.get_full_name()}")
        p.drawString(50, height - 170, f"Date of Birth: {student.date_of_birth.strftime('%B %d, %Y')}")
        p.drawString(50, height - 190, f"Gender: {student.get_gender_display()}")
        p.drawString(50, height - 210, f"School: {student.school.full_name}")

        # Add QR code if exists
        if student.qr_code:
            qr_path = os.path.join(settings.MEDIA_ROOT, student.qr_code.name)
            if os.path.exists(qr_path):
                p.drawImage(qr_path, width - 200, height - 200, width=150, height=150)

        # Add border
        p.setStrokeColor(colors.black)
        p.rect(30, 30, width - 60, height - 60)

        p.showPage()
        p.save()
        
        return response

