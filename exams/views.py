from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   
from exams.models import Exam
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'exams/exam_list.html'
    context_object_name = 'exams'

class ExamDetailView(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = 'exams/exam_detail.html'
    context_object_name = 'exam'

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    template_name = 'exams/exam_form.html'
    fields = ['exam_term', 'exam_date', 'exam_time', 'exam_subject', 'exam_class', 'full_marks', 'pass_marks', 'theory_marks', 'practical_marks', 'credit_hours', 'exam_level', 'exam_status']
    success_url = reverse_lazy('exam.index')

class ExamUpdateView(LoginRequiredMixin, UpdateView):
    model = Exam
    template_name = 'exams/exam_form.html'
    fields = ['exam_term', 'exam_date', 'exam_time', 'exam_subject', 'exam_class', 'full_marks', 'pass_marks', 'theory_marks', 'practical_marks', 'credit_hours', 'exam_level', 'exam_status']
    success_url = reverse_lazy('exam.index')

class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exams/exam_confirm_delete.html'
    context_object_name = 'exam'
    success_url = reverse_lazy('exam.index')