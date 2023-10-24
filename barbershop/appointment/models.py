from django.db import models
from barbershop.models import Barbers

class Appointment(models.Model):
    dt = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    barber = models.CharField(max_length=100, blank=True, null=True)
    service = models.CharField(max_length=250, blank=True, null=True)
    day = models.DateField()
    time = models.TimeField()
    brbr = models.ForeignKey(Barbers, on_delete=models.CASCADE, null=True)

    def __sts__(self):
        return self.name
