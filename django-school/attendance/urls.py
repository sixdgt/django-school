from django.urls import path
from attendance.views import (
    AttendanceListView, AttendanceDetailView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView,
    StudentAttendanceListView, StudentAttendanceDetailView, StudentAttendanceCreateView, StudentAttendanceUpdateView, StudentAttendanceDeleteView,
    TeacherAttendanceListView, TeacherAttendanceDetailView, TeacherAttendanceCreateView, TeacherAttendanceUpdateView, TeacherAttendanceDeleteView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # General Attendance (legacy)
    path('', login_required(AttendanceListView.as_view()), name='attendance.index'),
    path('<int:pk>/', login_required(AttendanceDetailView.as_view()), name='attendance.detail'),
    path('create/', login_required(AttendanceCreateView.as_view()), name='attendance.create'),
    path('<int:pk>/edit/', login_required(AttendanceUpdateView.as_view()), name='attendance.update'),
    path('<int:pk>/delete/', login_required(AttendanceDeleteView.as_view()), name='attendance.delete'),

    # Student Attendance
    path('students/', login_required(StudentAttendanceListView.as_view()), name='attendance.student.index'),
    path('students/create/', login_required(StudentAttendanceCreateView.as_view()), name='attendance.student.create'),
    path('students/<int:pk>/', login_required(StudentAttendanceDetailView.as_view()), name='attendance.student.detail'),
    path('students/<int:pk>/edit/', login_required(StudentAttendanceUpdateView.as_view()), name='attendance.student.update'),
    path('students/<int:pk>/delete/', login_required(StudentAttendanceDeleteView.as_view()), name='attendance.student.delete'),

    # Teacher Attendance
    path('teachers/', login_required(TeacherAttendanceListView.as_view()), name='attendance.teacher.index'),
    path('teachers/create/', login_required(TeacherAttendanceCreateView.as_view()), name='attendance.teacher.create'),
    path('teachers/<int:pk>/', login_required(TeacherAttendanceDetailView.as_view()), name='attendance.teacher.detail'),
    path('teachers/<int:pk>/edit/', login_required(TeacherAttendanceUpdateView.as_view()), name='attendance.teacher.update'),
    path('teachers/<int:pk>/delete/', login_required(TeacherAttendanceDeleteView.as_view()), name='attendance.teacher.delete'),
]