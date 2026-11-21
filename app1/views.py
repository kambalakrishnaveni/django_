

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1 style="color:green;">Welcome to Django first class</h1>')
