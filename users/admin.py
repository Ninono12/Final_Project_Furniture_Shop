from django.contrib import admin
from .models import CustomUserProfile


@admin.register(CustomUserProfile)
class CustomUserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "phone")
    search_fields = ("first_name", "last_name", "phone")
