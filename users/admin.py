from .models import CustomUser
from django.contrib import admin
#from .models import Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone', 'birth_date')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('birth_date',)

#@admin.register(Profile)
#class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user', 'first_name', 'last_name', 'phone', 'address', 'birth_date')

