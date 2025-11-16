from django.db import models
from django.conf import settings


class CustomUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='custom_profile'
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
