from django.contrib import admin

from Workshop.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'publication_date', 'location', 'pets', 'description']

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'
