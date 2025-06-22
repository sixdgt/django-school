from django.urls import path
from .views import AssignmentListView, AssignmentCreateView, AssignmentUpdateView, AssignmentDeleteView, AssignmentDetailView

urlpatterns = [
    path('', AssignmentListView.as_view(), name='assignment.index'),
    path('create/', AssignmentCreateView.as_view(), name='assignment.create'),
    path('detail/<int:pk>/', AssignmentDetailView.as_view(), name='assignment.detail'),
    path('update/<int:pk>/', AssignmentUpdateView.as_view(), name='assignment.update'),
    path('delete/<int:pk>/', AssignmentDeleteView.as_view(), name='assignment.delete'),
]