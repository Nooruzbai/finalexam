from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView

from webapp.forms import AdvertisementForm
from webapp.models import Advertisement

User = get_user_model()


class AdvertisementListView(ListView):
    template_name = 'index.html'
    model = Advertisement
    context_object_name = "advertisments"
    paginate_by = 5
    paginate_orphans = 0
    # search_fields = ["title__icontains", "author__icontains"]
    ordering = ["-date_created"]


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "create.html"
    permission_required = "webapp.add_article"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)