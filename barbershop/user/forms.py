from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']

        labels = {#название поля будет отображаться как Name в html а не first_name
            'username': 'Никнейм',
            'first_name': 'Ваше имя'
        }
