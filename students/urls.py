from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentDetailView,
    StudentUpdateView, StudentDeleteView, StudentIDCardView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', StudentListView.as_view(), name='student.index'),
    path('create/', StudentCreateView.as_view(), name='student.create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student.detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student.update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student.delete'),
    path('<int:pk>/id-card/', StudentIDCardView.as_view(), name='student.id_card'),
]