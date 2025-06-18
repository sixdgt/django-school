from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView       
from teachers.models import Teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['teacher_name', 'teacher_email', 'teacher_phone', 'teacher_address', 'teacher_gender', 'academic_level', 'teacher_date_of_birth', 'teacher_date_of_joining', 'teacher_date_of_leaving']
    success_url = reverse_lazy('teacher.index')

class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['teacher_name', 'teacher_email', 'teacher_phone', 'teacher_address', 'teacher_gender', 'academic_level', 'teacher_date_of_birth', 'teacher_date_of_joining', 'teacher_date_of_leaving']
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher.index')