from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from eremchenko_kv import settings
from eremchenko_kv.views.index import index_page
from fut_in_pst_typology.views.home import home_page
from fut_in_pst_typology.views.langauge import language_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('fut-in-pst-typology/', home_page),
    path('fut-in-pst-typology/language', language_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
