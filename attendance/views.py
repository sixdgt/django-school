from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   
from attendance.models import Attendance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'attendances'

class AttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attendance/attendance_detail.html'
    context_object_name = 'attendance'

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = 'attendance/attendance_form.html'
    fields = ['student', 'date', 'status', 'subject', 'class_name', 'teacher']
    success_url = reverse_lazy('attendance.index')

class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    template_name = 'attendance/attendance_form.html'
    fields = ['student', 'date', 'status', 'subject', 'class_name', 'teacher']
    success_url = reverse_lazy('attendance.index')

class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance/attendance_confirm_delete.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance.index')