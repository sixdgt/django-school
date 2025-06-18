from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   
from results.models import Result
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'results/result_list.html'
    context_object_name = 'results'

class ResultDetailView(LoginRequiredMixin, DetailView):
    model = Result
    template_name = 'results/result_detail.html'
    context_object_name = 'result'

class ResultCreateView(LoginRequiredMixin, CreateView):
    model = Result
    template_name = 'results/result_form.html'
    fields = ['result_name', 'result_date', 'result_class', 'result_student', 'result_subject', 'result_marks', 'result_status', 'result_grade', 'result_remarks', 'result_percentage', 'result_rank']
    success_url = reverse_lazy('result.index')

class ResultUpdateView(LoginRequiredMixin, UpdateView):
    model = Result
    template_name = 'results/result_form.html'
    fields = ['result_name', 'result_date', 'result_class', 'result_student', 'result_subject', 'result_marks', 'result_status', 'result_grade', 'result_remarks', 'result_percentage', 'result_rank']
    success_url = reverse_lazy('result.index')

class ResultDeleteView(LoginRequiredMixin, DeleteView):
    model = Result
    template_name = 'results/result_confirm_delete.html'
    context_object_name = 'result'
    success_url = reverse_lazy('result.index')