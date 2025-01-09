from django.contrib import admin

from Workshop.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth']
