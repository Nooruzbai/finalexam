from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from webapp.forms import AdvertisementForm
from webapp.models import Advertisement
from webapp.base import SearchView

User = get_user_model()


class AdvertisementListView(SearchView):
    template_name = 'index.html'
    model = Advertisement
    context_object_name = "advertisments"
    paginate_by = 5
    paginate_orphans = 0
    ordering = ["-date_created"]
    search_fields = ['headline']


class AdvertisementCreateView(PermissionRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "create.html"
    permission_required = "webapp.add_advertisement"
    success_url = reverse_lazy('webapp:webapp_list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class AdvertisementDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Advertisement
    context_object_name = 'advertisement'
    permission_required = "webapp.view_advertisement"


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = "delete.html"
    context_object_name = 'advertisement'
    permission_required = "webapp.delete_advertisement"
    success_url = reverse_lazy('webapp:webapp_list')

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:webapp_list', kwargs={"pk": self.object.pk})


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AdvertisementForm
    template_name = "update.html"
    model = Advertisement
    permission_required = "webapp.change_advertisement"

    # def has_permission(self):
    #     return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:advertisement_detail', kwargs={'pk': self.object.pk})


