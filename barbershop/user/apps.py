from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = 'Профили клиентов'

    def ready(self):
        import user.signals
