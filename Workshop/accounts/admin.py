from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


@admin.register(get_user_model())
class AppUserAdmin(auth_admin.UserAdmin):
    pass

