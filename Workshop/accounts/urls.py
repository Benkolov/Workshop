from django.urls import path, include

from Workshop.accounts.views import SignInView, SignUpView, UserDetailsView, UserEditView, UserDeleteView, SignOutView

urlpatterns = [
    path('login/', SignInView.as_view(), name='user login'),
    path('register/', SignUpView.as_view(), name='user register'),
    path('logout/', SignOutView.as_view(), name='user logout'),

    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
]
