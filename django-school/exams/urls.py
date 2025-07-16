from django.urls import path
from exams.views import (
    ExamListView, ExamDetailView, ExamCreateView, ExamUpdateView, ExamDeleteView,
    ExamSubjectListView, ExamSubjectDetailView, ExamSubjectCreateView, ExamSubjectUpdateView, ExamSubjectDeleteView,
    ExamLedgerListView, ExamLedgerDetailView, ExamLedgerCreateView, ExamLedgerUpdateView, ExamLedgerDeleteView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ExamListView.as_view()), name='exam.index'),
    path('<int:pk>/', login_required(ExamDetailView.as_view()), name='exam.detail'),
    path('create/', login_required(ExamCreateView.as_view()), name='exam.create'),
    path('<int:pk>/edit/', login_required(ExamUpdateView.as_view()), name='exam.update'),
    path('<int:pk>/delete/', login_required(ExamDeleteView.as_view()), name='exam.delete'),

    # ExamSubject CRUD
    path('<int:exam_id>/subjects/', login_required(ExamSubjectListView.as_view()), name='examsubject_list'),
    path('subjects/<int:pk>/', login_required(ExamSubjectDetailView.as_view()), name='examsubject.detail'),
    path('<int:exam_id>/subjects/create/', login_required(ExamSubjectCreateView.as_view()), name='examsubject.create'),
    path('subjects/<int:pk>/edit/', login_required(ExamSubjectUpdateView.as_view()), name='examsubject.update'),
    path('subjects/<int:pk>/delete/', login_required(ExamSubjectDeleteView.as_view()), name='examsubject.delete'),

    # ExamLedger CRUD
    path('subjects/<int:examsubject_id>/ledgers/', login_required(ExamLedgerListView.as_view()), name='examledger_list'),
    path('ledgers/<int:pk>/', login_required(ExamLedgerDetailView.as_view()), name='examledger.detail'),
    path('subjects/<int:examsubject_id>/ledgers/create/', login_required(ExamLedgerCreateView.as_view()), name='examledger.create'),
    path('ledgers/<int:pk>/edit/', login_required(ExamLedgerUpdateView.as_view()), name='examledger.update'),
    path('ledgers/<int:pk>/delete/', login_required(ExamLedgerDeleteView.as_view()), name='examledger.delete'),
]

