from django.contrib import admin
from .models import Barbers, Price, Portfolio

class BarbersAdmin(admin.ModelAdmin):
    list_display = ('id', 'barber_name', 'created')
    list_display_links = ('id', 'barber_name')
    search_fields = ('id', 'barber_name')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    search_fields = ('service', 'price')

class PorfolioAdmin(admin.ModelAdmin):
    list_display = ('image_small', 'image_big', 'end_photo_title', 'barber')
    list_display_links = ('barber', 'end_photo_title')
    list_filter = ('barber',)

admin.site.register(Barbers, BarbersAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Portfolio, PorfolioAdmin)