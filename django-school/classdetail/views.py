from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from classdetail.models import ClassDetail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class ClassDetailListView(LoginRequiredMixin, ListView):
    model = ClassDetail
    template_name = 'classdetail/classdetail_list.html'
    context_object_name = 'classdetails'

class ClassDetailView(LoginRequiredMixin, DetailView):
    model = ClassDetail
    template_name = 'classdetail/classdetail_detail.html'
    context_object_name = 'classdetail'

class ClassDetailCreateView(LoginRequiredMixin, CreateView):
    model = ClassDetail
    template_name = 'classdetail/classdetail_form.html'
    fields = ['class_name', 'class_teacher', 'class_type', 'class_status']
    success_url = reverse_lazy('classdetail.index')

class ClassDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = ClassDetail
    template_name = 'classdetail/classdetail_form.html'
    fields = ['class_name', 'class_teacher', 'class_type', 'class_status']
    success_url = reverse_lazy('classdetail.index')

class ClassDetailDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassDetail
    template_name = 'classdetail/classdetail_confirm_delete.html'
    context_object_name = 'classdetail'
    success_url = reverse_lazy('classdetail.index')