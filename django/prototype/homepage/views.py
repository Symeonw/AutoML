from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>TunaAI Homepage")

def about(request):
    return HttpResponse("<h1>TunaAI About Page")
