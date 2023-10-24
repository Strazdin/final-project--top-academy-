from django.db import models
from barbershop.models import Barbers

class Appointment(models.Model):
    dt = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    barber = models.CharField(max_length=100, blank=True, null=True, verbose_name="Барбер")
    service = models.CharField(max_length=250, blank=True, null=True, verbose_name="Услуга")
    day = models.DateField(verbose_name="День")
    time = models.TimeField(verbose_name="Время")
    brbr = models.ForeignKey(Barbers, on_delete=models.CASCADE, null=True, verbose_name="Барбер")

    def __sts__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-dt']
