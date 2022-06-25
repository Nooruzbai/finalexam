from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView, DetailView
from accounts.forms import MyUserCreationForm


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     images = self.object.image_s.all()
    #     galleries = self.object.gallerie_s.all()
    #     favourite_images = self.object.image_s.filter(private=True)
    #     context['images'] = images
    #     context['galleries'] = galleries
    #     context['favourite'] = favourite_images
    #     return context
