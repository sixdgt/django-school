from django.urls import path
from subjects.views import SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(SubjectListView.as_view()), name='subject.index'),
    path('<int:pk>/', login_required(SubjectDetailView.as_view()), name='subject.detail'),
    path('create/', login_required(SubjectCreateView.as_view()), name='subject.create'),
    path('<int:pk>/edit/', login_required(SubjectUpdateView.as_view()), name='subject.update'),
    path('<int:pk>/delete/', login_required(SubjectDeleteView.as_view()), name='subject.delete'),
]
