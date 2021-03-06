from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView

from webapp.base import SearchView
from webapp.models import Advertisement


class ModeratorList(PermissionRequiredMixin, ListView):
    template_name = 'moderators_page.html'
    model = Advertisement
    context_object_name = "advertisements"
    paginate_by = 5
    paginate_orphans = 0
    ordering = ["-date_created"]
    permission_required = "webapp.view_advertisement"

    def get_queryset(self):
        return super().get_queryset().filter(status="to_moderate")


class AdModeratorUpdate(PermissionRequiredMixin, DetailView):
    template_name = 'advertisment_operator_detail.html'
    model = Advertisement
    context_object_name = 'advertisement'
    permission_required = "webapp.view_advertisement"
