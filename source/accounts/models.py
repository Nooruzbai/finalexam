from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE, verbose_name='Profile')
    phone_number = PhoneNumberField(unique=True, region="KG", max_length=100, verbose_name="Phone number")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        permissions = []

    def __str__(self):
        return f"Profile: {self.user}. {self.id}"
