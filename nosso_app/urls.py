from django.urls import path
from .views import cadastro, home, cursos, contato

urlpatterns = [
        path('', home, name='home'),
        path('cursos/', cursos, name='cursos'),
        path('contato/', contato, name='contato'),
        path('cadastro/', cadastro, name='cadastro'),
    ]