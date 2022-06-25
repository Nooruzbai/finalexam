from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
CHOICES = [('to_moderate', 'To Moderate'), ('published', 'Published'), ('canceled', 'Canceled')]


class Advertisement(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False, verbose_name="Category")
    image = models.ImageField(upload_to="images/", null=False, blank=False, verbose_name="Image")
    headline = models.CharField(max_length=100, null=False, blank=False, verbose_name="Headline")
    description = models.TextField(max_length=100, null=True, blank=False, verbose_name="Description")
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2, verbose_name="Price")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    date_edited = models.DateTimeField(auto_now_add=True, verbose_name="Date edited")
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="Date published")
    status = models.CharField(default=CHOICES[0], choices=CHOICES, max_length=100, null=False, blank=False, verbose_name="Status")
    author = models.ForeignKey("accounts.Profile", null=False, blank=False, on_delete=models.CASCADE, related_name="advertisements", verbose_name="Advertisement")

    def __str__(self):
        return f"{self.pk}. {self.headline} {self.category} {self.date_created}"

    class Meta:
        db_table = "advertisement"
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    advertisement = models.ForeignKey('webapp.Advertisement', null=False, blank=False, on_delete=models.CASCADE, related_name="categories", verbose_name="Advertisement")

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
