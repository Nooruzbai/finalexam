from django.urls import path

from webapp.views import WebAppListView

app_name = 'webapp'

urlpatterns = [
    path('', WebAppListView.as_view(), name='webapp_list'),
]