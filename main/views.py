from django.shortcuts import render
from users.models import User


def home(request):
    context = {"users": User.objects.all()}
    return render(request, 'main/home.html', context=context)


def about(request):
    return render(request, 'main/about.html')
