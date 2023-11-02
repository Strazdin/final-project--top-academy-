from django.db import models
from barbershop.models import Barbers, Price
from user.models import Profile

class Appointment(models.Model):
    dt = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    day = models.DateField(verbose_name="День")
    time = models.TimeField(verbose_name="Время")
    barber = models.ForeignKey(Barbers, on_delete=models.CASCADE, null=True, verbose_name="Барбер")
    service = models.ForeignKey(Price, on_delete=models.SET_NULL, max_length=250, null=True, verbose_name="Услуга")
    client = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)

    def __sts__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-dt']
