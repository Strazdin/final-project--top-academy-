from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.user_account, name='user_account'),
]