from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from eremchenko_kv import settings
from eremchenko_kv.views.index import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
