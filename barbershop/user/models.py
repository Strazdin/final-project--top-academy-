from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Имя")
    phone_number = models.CharField(max_length=12, blank=True, null=True, unique=True, verbose_name="Номер телефона")
    username = models.CharField(max_length=200, blank=True, null=True, unique=True, verbose_name="Никнейм")
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Был добавлен")

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-created']
