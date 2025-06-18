from django.urls import path
from teachers.views import TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(TeacherListView.as_view()), name='teacher.index'),
    path('<int:pk>/', login_required(TeacherDetailView.as_view()), name='teacher.detail'),
    path('create/', login_required(TeacherCreateView.as_view()), name='teacher.create'),
    path('<int:pk>/edit/', login_required(TeacherUpdateView.as_view()), name='teacher.update'),
    path('<int:pk>/delete/', login_required(TeacherDeleteView.as_view()), name='teacher.delete'),
]
