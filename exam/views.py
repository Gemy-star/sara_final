from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, ListView

from . import models
from django.contrib import messages


def create_cat(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat_desc = request.POST.get('cat_desc')
        cat = models.Category(name=cat_name, description=cat_desc)
        if cat is not None:
            return render(request, 'exam/cat-detail.html', context={"cat": cat})
        else:
            messages.info(request, 'Error Occured')

    return render(request, 'exam/create-cat.html')


def cat_detail(request, pk):
    cat = models.Category.objects.get(pk=pk)
    return render(request, 'exam/cat-detail.html', context={"cat": cat})


def cat_edit(request, pk):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat_desc = request.POST.get('cat_desc')
        models.Category.objects.filter(pk=pk).update(name=cat_name, description=cat_desc)
        return render(request, 'exam/cat-detial.html', context={"cat": models.Category.objects.get(pk=pk)})
    return render(request, 'exam/cat-update.html', context={"cat": models.Category.objects.get(pk=pk)})


def cat_list(request):
    return render(request, 'exam/cat_list.html', context={"cats": models.Category.objects.all()})


class DeleteCatView(DeleteView):
    model = models.Category
    template_name = 'exam/cat-delete.html'
    context_object_name = 'cat'
    success_url = reverse_lazy('home-page')
    login_url = 'login'


class CreateExamView(LoginRequiredMixin, CreateView):
    model = models.Exam
    template_name = 'exam/create_exam.html'
    fields = '__all__'
    login_url = 'login'


class UpdateExamView(LoginRequiredMixin, UpdateView):
    model = models.Exam
    context_object_name = 'exam'
    template_name = 'exam/update_exam.html'
    fields = '__all__'
    login_url = 'login'


class DeleteExamView(DeleteView):
    model = models.Exam
    template_name = 'exam/exam_delete.html'
    context_object_name = 'exam'
    success_url = reverse_lazy('home-page')
    login_url = 'login'


class ListExamView(LoginRequiredMixin, ListView):
    model = models.Exam
    template_name = 'exam/exam_list.html'
    context_object_name = 'exams'
    paginate_by = 5
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListExamView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context


def detail_exam(request, pk):
    return render(request, 'exam/exam_detail.html', context={"exam": models.Exam.objects.get(pk=pk)})


class CreateQuestionView(LoginRequiredMixin, CreateView):
    model = models.Question
    template_name = 'exam/create_question.html'
    fields = '__all__'
    login_url = 'login'


class UpdateQuestionView(LoginRequiredMixin, UpdateView):
    model = models.Question
    context_object_name = 'question'
    template_name = 'exam/update_question.html'
    fields = '__all__'
    login_url = 'login'


class DeleteQuestionView(DeleteView):
    model = models.Question
    template_name = 'exam/question_delete.html'
    context_object_name = 'question'
    success_url = reverse_lazy('home-page')
    login_url = 'login'


class ListQuestionView(LoginRequiredMixin, ListView):
    model = models.Question
    template_name = 'exam/question_list.html'
    context_object_name = 'questions'
    paginate_by = 5
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListQuestionView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context


def detail_question(request, pk):
    return render(request, 'exam/question_detail.html', context={"question": models.Question.objects.get(pk=pk)})


def final_result_detail(request, pk):
    return render(request, 'exam/final_result_detail', context={"result": models.FinalResult.objects.get(pk=pk)})





class CreateSetView(LoginRequiredMixin, CreateView):
    model = models.Set
    template_name = 'exam/create_set.html'
    fields = '__all__'
    login_url = 'login'


class UpdateSetView(LoginRequiredMixin, UpdateView):
    model = models.Set
    context_object_name = 'set'
    template_name = 'exam/update_set.html'
    fields = '__all__'
    login_url = 'login'


class DeleteSetView(DeleteView):
    model = models.Set
    template_name = 'exam/set_delete.html'
    context_object_name = 'set'
    success_url = reverse_lazy('home-page')
    login_url = 'login'


class ListSetView(LoginRequiredMixin, ListView):
    model = models.Set
    template_name = 'exam/set_list.html'
    context_object_name = 'sets'
    paginate_by = 5
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(ListSetView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context


def detail_set(request, pk):
    return render(request, 'exam/set_detail.html', context={"set": models.Set.objects.get(pk=pk)})