from django.urls import path

from webapp.views import AdvertisementListView, AdvertisementCreateView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='webapp_list'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name="advertisement_create"),
]
