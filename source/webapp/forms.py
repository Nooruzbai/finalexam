from django import forms

from webapp.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ("headline", "image", "description", "category",)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Search')