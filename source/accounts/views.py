from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView, DetailView
from accounts.forms import MyUserCreationForm
from webapp.models import Advertisement


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('project_list_view')
        return next_url


class UserDetailView(DetailView):
    template_name = 'user_detailed_view.html'
    model = User
    context_object_name = 'user_object'
    paginate_by = 10
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        advertisements = Advertisement.objects.filter(author=self.object.pk)
        if advertisements.filter(Q(status='to_moderate') | Q(status='canceled') | Q(status='published')):
            kwargs["advertisements"] = advertisements
            return super().get_context_data(**kwargs)

