from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, get_csrf_token, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="registration"),
    path("user/<int:pk>/details/", UserDetailView.as_view(), name="user_detailed_view"),
    path("get-csrf-token/", get_csrf_token, name="get_csrf_token"),
]
