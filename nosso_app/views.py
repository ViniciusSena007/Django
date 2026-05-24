from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')
# Create your views here.
