from django.contrib import admin
from .models import Barbers, Price
# Register your models here.

class BarbersAdmin(admin.ModelAdmin):
    list_display = ('id', 'barber_name', 'created')
    list_display_links = ('id', 'barber_name')
    search_fields = ('id', 'barber_name')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    search_fields = ('service', 'price')

admin.site.register(Barbers, BarbersAdmin)
admin.site.register(Price, PriceAdmin)