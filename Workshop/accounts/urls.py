from django.urls import path, include

from Workshop.accounts.views import details_user, edit_user, delete_user, SignInView, SignUpView

urlpatterns = [
    path('login/', SignInView.as_view(), name='user login'),
    path('register/', SignUpView.as_view(), name='user register'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='delete user'),
    ])),
]
