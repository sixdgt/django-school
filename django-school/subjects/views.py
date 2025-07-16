from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from subjects.models import Subject
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subjects/subject_list.html'
    context_object_name = 'subjects'

class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'
    context_object_name = 'subject'

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    template_name = 'subjects/subject_form.html'
    fields = ['subject_name', 'subject_code', 'subject_description', 'class_name', 'subject_teacher', 'subject_type', 'credit_hours', 'subject_status']
    success_url = reverse_lazy('subject.index')

class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    template_name = 'subjects/subject_form.html'
    fields = ['subject_name', 'subject_code', 'subject_description', 'class_name', 'subject_teacher', 'subject_type', 'credit_hours', 'subject_status']
    success_url = reverse_lazy('subject.index')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name = 'subjects/subject_confirm_delete.html'
    context_object_name = 'subject'
    success_url = reverse_lazy('subject.index')