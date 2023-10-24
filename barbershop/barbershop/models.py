from django.db import models

class Barbers(models.Model):
    barber_name = models.CharField(max_length=100, db_index=True, verbose_name="Имя")
    barber_image = models.ImageField(upload_to='barbers/images/')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Был добавлен")

    def __str__(self):
        return self.barber_name
    
    class Meta:
        verbose_name = 'Барбера'
        verbose_name_plural = 'Барберы'
        ordering = ['-created']
    
class Price(models.Model):
    service = models.CharField(max_length=200, db_index=True, verbose_name="Название услуги")
    price = models.IntegerField(default=0, null=True, blank=True, verbose_name="Цена")

    def __str__(self):
        return self.service
    
    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Прайс-лист'
        ordering = ['-price']