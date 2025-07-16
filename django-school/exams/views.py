from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   
from exams.models import Exam, ExamSubject, ExamLedger
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
    fields = ['exam_term', 'exam_date', 'exam_time', 'exam_subject', 'exam_class', 'exam_level', 'exam_academic_year', 'exam_status']
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

# ExamSubject Views
class ExamSubjectListView(LoginRequiredMixin, ListView):
    model = ExamSubject
    template_name = 'exams/examsubject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return ExamSubject.objects.filter(exam_id=self.kwargs['exam_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam'] = Exam.objects.get(pk=self.kwargs['exam_id'])
        return context

class ExamSubjectDetailView(LoginRequiredMixin, DetailView):
    model = ExamSubject
    template_name = 'exams/examsubject_detail.html'
    context_object_name = 'examsubject'

class ExamSubjectCreateView(LoginRequiredMixin, CreateView):
    model = ExamSubject
    template_name = 'exams/examsubject_form.html'
    fields = ['exam', 'exam_subject', 'full_marks', 'pass_marks', 'theory_marks', 'practical_marks', 'credit_hours']

    def get_initial(self):
        initial = super().get_initial()
        exam_id = self.kwargs.get('exam_id')
        if exam_id:
            initial['exam'] = exam_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam'] = Exam.objects.get(pk=self.kwargs['exam_id'])
        return context

    def form_valid(self, form):
        form.instance.exam_id = self.kwargs['exam_id']
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.exam.get_absolute_url()

class ExamSubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = ExamSubject
    template_name = 'exams/examsubject_form.html'
    fields = ['exam', 'exam_subject', 'full_marks', 'pass_marks', 'theory_marks', 'practical_marks', 'credit_hours']

    def get_success_url(self):
        return self.object.exam.get_absolute_url()

class ExamSubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = ExamSubject
    template_name = 'exams/examsubject_confirm_delete.html'
    context_object_name = 'examsubject'

    def get_success_url(self):
        return self.object.exam.get_absolute_url()

# ExamLedger Views
class ExamLedgerListView(LoginRequiredMixin, ListView):
    model = ExamLedger
    template_name = 'exams/examledger_list.html'
    context_object_name = 'ledgers'

    def get_queryset(self):
        return ExamLedger.objects.filter(exam_id=self.kwargs['examsubject_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examsubject'] = ExamSubject.objects.get(pk=self.kwargs['examsubject_id'])
        return context

class ExamLedgerDetailView(LoginRequiredMixin, DetailView):
    model = ExamLedger
    template_name = 'exams/examledger_detail.html'
    context_object_name = 'examledger'

class ExamLedgerCreateView(LoginRequiredMixin, CreateView):
    model = ExamLedger
    template_name = 'exams/examledger_form.html'
    fields = ['exam', 'student', 'obtained_marks', 'grade', 'grade_point', 'weighted_grade', 'remarks', 'exam_ledger_status']

    def get_initial(self):
        initial = super().get_initial()
        examsubject_id = self.kwargs.get('examsubject_id')
        if examsubject_id:
            initial['exam'] = examsubject_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examsubject'] = ExamSubject.objects.get(pk=self.kwargs['examsubject_id'])
        return context

    def form_valid(self, form):
        form.instance.exam_id = self.kwargs['examsubject_id']
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.exam.get_absolute_url()

class ExamLedgerUpdateView(LoginRequiredMixin, UpdateView):
    model = ExamLedger
    template_name = 'exams/examledger_form.html'
    fields = ['exam', 'student', 'obtained_marks', 'grade', 'grade_point', 'weighted_grade', 'remarks', 'exam_ledger_status']

    def get_success_url(self):
        return self.object.exam.get_absolute_url()

class ExamLedgerDeleteView(LoginRequiredMixin, DeleteView):
    model = ExamLedger
    template_name = 'exams/examledger_confirm_delete.html'
    context_object_name = 'examledger'

    def get_success_url(self):
        return self.object.exam.get_absolute_url()