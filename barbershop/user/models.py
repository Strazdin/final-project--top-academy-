from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    username = models.CharField(max_length=200, blank=True, null=True, unique=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, default='profiles/user-default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'
