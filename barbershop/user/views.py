from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Profile, User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm

from appointment.models import Appointment

# Create your views here.

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
    return redirect('/user/login/')

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username#.lower()
            user.save()
            messages.success(request, 'Учетная запись пользователя создана!')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Во время регистрации произошла ошибка!')
    context = {'page': page, 'form': form}
    return render(request, 'user/login_register.html', context)

@login_required(login_url='login')
def user_account(request):
    count_appointments = Appointment.objects.filter(client_id=request.user.id).count()
    prof = request.user.profile

    context = {
        'profile': prof,
        'count_appointments': count_appointments,
    }
    return render(request, 'user/account.html', context)

@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            if form.cleaned_data['phone_number'].isdigit() and len(form.cleaned_data['phone_number']) == 10:
                if form.cleaned_data['name'].isalpha() and len(form.cleaned_data['name']) >= 2:
                    profile = form.save(commit=False)
                    profile.name = form.cleaned_data['name'].capitalize()
                    profile.save()
                else:
                    messages.error(request, 'Имя должно состоять только из букв')
            else:
                messages.error(request, 'Номер телефона должен состоять из 10 цифр')


            return redirect('user_account')
    context = {'form': form}
    return render(request, 'user/profile-form.html', context)