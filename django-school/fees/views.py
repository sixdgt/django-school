from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from fees.models import Fee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class FeeListView(LoginRequiredMixin, ListView):
    model = Fee
    template_name = 'fees/fee_list.html'
    context_object_name = 'fees'

class FeeDetailView(LoginRequiredMixin, DetailView):
    model = Fee
    template_name = 'fees/fee_detail.html'
    context_object_name = 'fee'

class FeeCreateView(LoginRequiredMixin, CreateView):
    model = Fee
    template_name = 'fees/fee_form.html'
    fields = ['fee_name', 'fee_amount', 'fee_date', 'fee_class', 'fee_student', 'fee_status', 'fee_description', 'fee_payment_method', 'fee_payment_date', 'fee_payment_amount', 'fee_payment_status', 'fee_payment_description']
    success_url = reverse_lazy('fee.index')

class FeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Fee
    template_name = 'fees/fee_form.html'
    fields = ['fee_name', 'fee_amount', 'fee_date', 'fee_class', 'fee_student', 'fee_status', 'fee_description', 'fee_payment_method', 'fee_payment_date', 'fee_payment_amount', 'fee_payment_status', 'fee_payment_description']
    success_url = reverse_lazy('fee.index')

class FeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Fee
    template_name = 'fees/fee_confirm_delete.html'
    context_object_name = 'fee'
    success_url = reverse_lazy('fee.index') 
