from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   
from attendance.models import Attendance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from students.models import Student
from teachers.models import Teacher

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

# Student Attendance Views
class StudentAttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/student_attendance_list.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        return Attendance.objects.filter(student__isnull=False)

class StudentAttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = 'attendance/student_attendance_form.html'
    fields = ['student', 'date', 'status', 'subject', 'class_name']
    success_url = reverse_lazy('attendance.student.index')

class StudentAttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attendance/student_attendance_detail.html'
    context_object_name = 'attendance'

class StudentAttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    template_name = 'attendance/student_attendance_form.html'
    fields = ['student', 'date', 'status', 'subject', 'class_name']
    success_url = reverse_lazy('attendance.student.index')

class StudentAttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance/student_attendance_confirm_delete.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance.student.index')

# Teacher Attendance Views
class TeacherAttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'attendance/teacher_attendance_list.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        return Attendance.objects.filter(teacher__isnull=False)

class TeacherAttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = 'attendance/teacher_attendance_form.html'
    fields = ['teacher', 'date', 'status', 'subject', 'class_name']
    success_url = reverse_lazy('attendance.teacher.index')

class TeacherAttendanceDetailView(LoginRequiredMixin, DetailView):
    model = Attendance
    template_name = 'attendance/teacher_attendance_detail.html'
    context_object_name = 'attendance'

class TeacherAttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    template_name = 'attendance/teacher_attendance_form.html'
    fields = ['teacher', 'date', 'status', 'subject', 'class_name']
    success_url = reverse_lazy('attendance.teacher.index')

class TeacherAttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'attendance/teacher_attendance_confirm_delete.html'
    context_object_name = 'attendance'
    success_url = reverse_lazy('attendance.teacher.index')