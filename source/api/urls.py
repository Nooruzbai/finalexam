from django.urls import path

from api.views import ModerateStatus, CancelStatus

app_name = 'api'

urlpatterns = [
    path('api/moderate/<int:pk>', ModerateStatus.as_view(), name='moderate_status'),
    path('api/cancel/<int:pk>', CancelStatus.as_view(), name='cancel_status'),
]
