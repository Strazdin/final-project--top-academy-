from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']

        labels = {#название поля будет отображаться как Name в html а не first_name
            'username': 'Никнейм',
            'first_name': 'Ваше имя'
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'created']

        labels = {
            'username': 'Никнейм',
            'name': 'Ваше имя',
            'phone_number': 'Номер телефона',
            'profile_image': 'Фото профиля'
        }
