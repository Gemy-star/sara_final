from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse

from exam.models import Exam, Category, Question, FinalResult
from django.contrib import messages
from users.models import User


def create_exam(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        cat = request.POST.get('cat')
        result = request.POST.get('total_result')
        cat_obj = Category.objects.get(pk=cat)

        exam = Exam(name=question, TotalResult=result, category=cat_obj)

        if exam is not None:
            return redirect('create-question-page')
        else:
            messages.info(request, 'Data is not valid')
    cats = Category.objects.all()
    context = {"cats": cats}
    return render(request, 'exam/create-exam.html', context)


def create_question(request):
    if request.method == 'POST' and request.FILES['question_photo']:
        qtype = request.POST.get('qtype')
        exam = request.POST.get('exams')
        cat = request.POST.get('cat')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        question_photo = request.FILES['question_photo']
        fs = FileSystemStorage()
        filename = fs.save(question_photo.name, question_photo)
        cat_obj = Category.objects.get(pk=cat)
        exam_obj = Exam.objects.get(pk=exam)
        question_obj = Question(questionType=qtype, exam=exam_obj, category=cat_obj, question=question, answer=answer)
        if question_obj is not None:
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data ')
    context = {"exams": Exam.objects.all(), "cats": Category.objects.all()}
    return render(request, 'exam/create-question.html', context)


def create_result(request):
    if request.method == 'POST':
        result = request.POST.get('result')
        exam = request.POST.get('exam')
        user = request.POST.get('tester')
        exam_obj = Exam.objects.filter(pk=exam)
        user_obj = User.objects.filter(pk=user)

        final_result = FinalResult(result=result, exam=exam_obj, user=user_obj)

        if final_result is not None:
            return redirect('home-page')
        else:
            messages.info(request, 'Data is not valid')
    context = {"testers": User.objects.filter(user_type=2), "exams": Exam.objects.all()}
    return render(request, 'exam/create_result.html', context)


def cat_list(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'exam/cat_list.html', context=context)


def exam_list(request):
    context = {"exams": Exam.objects.all()}
    return render(request, 'exam/exam_list.html', context=context)


def exam_list_user(request, pk):
    context = {"exams": Exam.objects.filter(pk=pk)}
    return render(request, 'exam/exam_list.html', context=context)


def question_list_user(request, pk):
    ans = dict()
    result = dict()
    degree = 0
    exam = Exam.objects.get(pk=pk)
    question = Question.objects.filter(Exam=exam)
    user = request.user
    for ques in question:
        result[ques.question] = ques.answer
    if request.method == "POST":
        for q in question:
            answers = request.POST.get('questions' + str(q.pk))
            ans[q.question] = answers
        for key in ans:
            if ans[key] == result[key]:
                degree += 10
        r = FinalResult(user=user, exam=exam, result=degree)
        if r is not None:
            return render(request, 'exam/result_exam_list.html', context={"result": r})
        else:
            messages.info(request, 'Data is not valid')

    context = {"questions": question, "exam": exam}
    return render(request, 'exam/question_list.html', context=context)


def result_exam_list(request, pk):
    final_result = FinalResult.objects.get(pk=pk)
    content = {"result": final_result}
    return render(request, 'exam/result_exam_list.html', context=content)
