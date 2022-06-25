from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import Profile
from webapp.models import User


class ProfileInLine(admin.StackedInline):
    fields = ("id", "phone_number")
    model = Profile


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInLine,)


# admin.site.unregister(User)
admin.site.register(Profile)
