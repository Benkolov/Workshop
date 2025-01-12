from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views, generic
from django.contrib.auth import views as auth_view, get_user_model
from django.shortcuts import render

from Workshop.accounts.forms import UserCreateForm, UserModel
from Workshop.pets.models import Pet
from Workshop.photos.models import Photo


class SignInView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('accounts/login-page.html')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user ==  self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ['first_name', 'last_name', 'email', 'gender']

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
