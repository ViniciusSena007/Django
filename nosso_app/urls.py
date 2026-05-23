from django.urls import path
from .views import home
from nosso_app import views

urlpatterns = [
        path('', home, name='home'),
    ]