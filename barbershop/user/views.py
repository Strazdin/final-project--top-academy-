from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Profile, User
# Create your views here.

def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'user/profile.html', context)

def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    context = {'profile': prof}
    return render(request, 'user/profile.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Пользователь с таким именем не существует')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Имя пользователя или пароль неверны')

    return render(request, 'user/login_register.html')

def logout_user(request):
    logout(request)
    messages.error(request, 'Пользователь вышел из системы!')
    return redirect('/')
