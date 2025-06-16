from django.shortcuts import render
from modelpractice.models import School
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SchoolListView(LoginRequiredMixin, ListView):
    model = School
    template_name = 'index.html'
    context_object_name = 'school'
    ordering = ['-full_name']
    paginate_by = 10

class SchoolDetailView(LoginRequiredMixin, DetailView):
    model = School
    template_name = 'detail.html'
    context_object_name = 'school'

class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    template_name = 'school_form.html'
    fields = ['full_name', 'school_type']
    success_url = reverse_lazy('school.index')

class SchoolUpdateView(LoginRequiredMixin, UpdateView):
    model = School
    template_name = 'school_form.html'
    fields = ['full_name', 'school_type']
    success_url = reverse_lazy('school.index')

class SchoolDeleteView(LoginRequiredMixin, DeleteView):
    model = School
    success_url = reverse_lazy('school.index')
