from django.urls import path
from exams.views import ExamListView, ExamDetailView, ExamCreateView, ExamUpdateView, ExamDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ExamListView.as_view()), name='exam.index'),
    path('<int:pk>/', login_required(ExamDetailView.as_view()), name='exam.detail'),
    path('create/', login_required(ExamCreateView.as_view()), name='exam.create'),
    path('<int:pk>/edit/', login_required(ExamUpdateView.as_view()), name='exam.update'),
    path('<int:pk>/delete/', login_required(ExamDeleteView.as_view()), name='exam.delete'),\
]

