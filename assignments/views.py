from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Assignment
from django.urls import reverse_lazy

# Create your views here.
class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_index.html'
    context_object_name = 'assignments'

class AssignmentCreateView(CreateView):
    model = Assignment
    template_name = 'assignment_form.html'
    fields = ['title', 'start_date', 'end_date', 'question_file', 'question', 'remark', 'full_mark', 'teacher', 'assignment_subject', 'academic_year', 'class_name']
    success_url = reverse_lazy('assignment.index')

class AssignmentUpdateView(UpdateView):
    model = Assignment
    template_name = 'assignment_form.html'
    fields = ['title', 'start_date', 'end_date', 'question_file', 'question', 'remark', 'full_mark', 'teacher', 'assignment_subject', 'academic_year', 'class_name']
    success_url = reverse_lazy('assignment.index')

class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'assignment_confirm_delete.html'
    context_object_name = 'assignment'
    success_url = reverse_lazy('assignment.index')