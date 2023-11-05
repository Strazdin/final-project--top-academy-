from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('barber/', views.appointment_barber, name='appointment-barber'),
    path('thanks/', views.thanks_page, name='thanks_page'),
]