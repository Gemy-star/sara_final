from django.shortcuts import render, redirect
from exam.models import Exam, Category
from django.contrib import messages





def create_exam(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        cat = request.POST.get('cat')
        result = request.POST.get('t_result')

        exam = Exam(name=question, TotalResult=result, category=cat)

        if exam is not None:
            return redirect('home-page')
    exams = Category.objects.all()
    context = {"exams": exams}
    return render(request, 'exam/exam.html', context)


