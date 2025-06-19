from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Material
from django.urls import reverse_lazy

# Create your views here.
class MaterialListView(ListView):
    model = Material
    template_name = 'material_index.html'
    context_object_name = 'materials'

class MaterialCreateView(CreateView):
    model = Material
    template_name = 'material_form.html'
    fields = ['title', 'category', 'description', 'material_subject', 'academic_year', 'class_name', 'material_file', 'teacher']
    success_url = reverse_lazy('material.index')

class MaterialUpdateView(UpdateView):
    model = Material
    template_name = 'material_form.html'
    fields = ['title', 'category', 'description', 'material_subject', 'academic_year', 'class_name', 'material_file', 'teacher']
    success_url = reverse_lazy('material.index')

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'material_confirm_delete.html'
    context_object_name = 'material'
    success_url = reverse_lazy('material.index')

class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material_detail.html'
    context_object_name = 'material'
