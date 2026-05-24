from django.urls import path
from .views import home, cursos

urlpatterns = [
        path('', home, name='home'),
        path('cursos/', cursos, name='cursos'),
    ]