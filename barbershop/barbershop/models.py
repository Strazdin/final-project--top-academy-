from django.db import models

class Barbers(models.Model):
    barber_name = models.CharField(max_length=100)
    barber_image = models.ImageField(upload_to='barbers/images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
  