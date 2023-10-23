from django.urls import path
from . import views

app_name = 'barbershop'

urlpatterns = [
    path('', views.barbershop, name='barbershop')
]