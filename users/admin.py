from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone', 'birth_date')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('birth_date',)

