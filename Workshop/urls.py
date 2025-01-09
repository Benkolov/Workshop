from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Workshop.common.urls')),
    path('accounts/', include('Workshop.accounts.urls')),
    path('pets/', include('Workshop.pets.urls')),
    path('photos/', include('Workshop.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
