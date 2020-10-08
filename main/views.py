from django.shortcuts import render
from users.models import User
from exam.models import Category


def home(request):
    context = {"users": User.objects.filter(user_type=1), "cats": Category.objects.all()}
    return render(request, 'main/home.html', context=context)


def about(request):
    return render(request, 'main/about.html')
