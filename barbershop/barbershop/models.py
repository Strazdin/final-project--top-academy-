from django.db import models

class Barbers(models.Model):
    barber_name = models.CharField(max_length=100, db_index=True)
    barber_image = models.ImageField(upload_to='barbers/images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barber_name
    
class Price(models.Model):
    service = models.CharField(max_length=200)
    price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.service