from django.contrib import admin

from django.contrib import admin

from webapp.models import Advertisement, Category


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', "headline", "category"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Category, CategoryAdmin)