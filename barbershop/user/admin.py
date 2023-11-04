from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'phone_number', 'created')
    list_display_links = ('id', 'username')
    search_fields = ('id', 'username', 'phone_number', 'name')
    list_filter = ('created',)

admin.site.register(Profile, ProfileAdmin)