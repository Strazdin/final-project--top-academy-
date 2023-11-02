from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
]