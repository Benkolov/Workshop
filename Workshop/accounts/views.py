from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views, View
from django.contrib.auth import views as auth_view, logout, login

from Workshop.accounts.forms import UserCreateForm, UserModel


class SignInView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)

        return response

class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('user login'))


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
