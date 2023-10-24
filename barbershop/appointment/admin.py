from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'barber', 'service', 'day', 'time')
    search_fields = ('id', 'name', 'barber', 'service', 'day', 'time')

admin.site.register(Appointment, AppointmentAdmin)
