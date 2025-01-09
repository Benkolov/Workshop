from django.contrib import admin

from Workshop.common.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'publication_date_and_time']


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']
