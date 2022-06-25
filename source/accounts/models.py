from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE, verbose_name='Profile')
    phone_number = PhoneNumberField(region="KG", max_length=13)
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Firstname")
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Lastname")

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        permissions = []

    def __str__(self):
        return f"Profile: {self.user}. {self.id} {self.last_name} {self.first_name}, {self.phone_number} "
