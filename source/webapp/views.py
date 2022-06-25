from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class WebAppListView(ListView):
    template_name = 'index.html'