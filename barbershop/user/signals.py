from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver
from .models import Profile, User

@receiver(post_save, sender=User)
def profile_update(instance, created, **kwargs):
    print('User signal!')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            name=user.first_name,
        )

@receiver(post_save, sender=Profile)
def update_user(instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created is False:
        user.first_name = profile.name
        user.username = profile.username
        user.save()

@receiver(post_delete, sender=Profile)
def profile_delete(instance, **kwargs):
    user = instance.user
    user.delete()