from django.urls import path
from attendance.views import AttendanceListView, AttendanceDetailView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(AttendanceListView.as_view()), name='attendance.index'),
    path('<int:pk>/', login_required(AttendanceDetailView.as_view()), name='attendance.detail'),
    path('create/', login_required(AttendanceCreateView.as_view()), name='attendance.create'),
    path('<int:pk>/edit/', login_required(AttendanceUpdateView.as_view()), name='attendance.update'),
    path('<int:pk>/delete/', login_required(AttendanceDeleteView.as_view()), name='attendance.delete'),
]