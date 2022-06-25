from django.urls import path

from webapp.moderator import ModeratorList, AdModeratorUpdate
from webapp.views import AdvertisementListView, AdvertisementCreateView, AdvertisementDetailView, \
    AdvertisementDeleteView, AdvertisementUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='webapp_list'),
    path('advertisement/create/', AdvertisementCreateView.as_view(), name="advertisement_create"),
    path('advertisement/<int:pk>/detail', AdvertisementDetailView.as_view(), name="advertisement_detail"),
    path('advertisement/<int:pk>/delete', AdvertisementDeleteView.as_view(), name="advertisement_delete"),
    path('advertisement/<int:pk>/update', AdvertisementUpdateView.as_view(), name="advertisement_update"),
    path('advertisement/list', ModeratorList.as_view(), name="moderator_list"),
    path('advertisement/operator/<int:pk>/detail', AdModeratorUpdate.as_view(), name="advertisement_operator_detail"),


]
