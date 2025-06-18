from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView       
from libraries.models import Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class LibraryListView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'libraries/library_list.html'
    context_object_name = 'libraries'  

class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library 
    template_name = 'libraries/library_detail.html'
    context_object_name = 'library'

class LibraryCreateView(LoginRequiredMixin, CreateView):
    model = Library
    template_name = 'libraries/library_form.html'
    fields = ['book_name', 'book_author', 'book_publisher', 'book_publication_date', 'book_isbn', 'book_category', 'book_quantity', 'book_price', 'book_description', 'book_status', 'book_location', 'book_shelf', 'book_row', 'book_column', 'book_level', 'book_section', 'book_sub_section', 'book_rack_number', 'book_shelf_number', 'book_row_number', 'book_column_number', 'book_level_number', 'book_section_number', 'book_sub_section_number']
    success_url = reverse_lazy('library.index')

class LibraryUpdateView(LoginRequiredMixin, UpdateView):
    model = Library
    template_name = 'libraries/library_form.html'
    fields = ['book_name', 'book_author', 'book_publisher', 'book_publication_date', 'book_isbn', 'book_category', 'book_quantity', 'book_price', 'book_description', 'book_status', 'book_location', 'book_shelf', 'book_row', 'book_column', 'book_level', 'book_section', 'book_sub_section', 'book_rack_number', 'book_shelf_number', 'book_row_number', 'book_column_number', 'book_level_number', 'book_section_number', 'book_sub_section_number']
    success_url = reverse_lazy('library.index')    

class LibraryDeleteView(LoginRequiredMixin, DeleteView):
    model = Library
    template_name = 'libraries/library_confirm_delete.html'
    context_object_name = 'library'
    success_url = reverse_lazy('library.index')