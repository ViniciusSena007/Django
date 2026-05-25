from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import CadastroForm

def home(request):
    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')

def contato(request):
    return render(request, 'contato.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Cadastro realizado com sucesso!')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})
# Create your views here.
