from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from pwa.urls import urlpatterns as pwa_urlpatterns

from eremchenko_kv import settings
from eremchenko_kv.views.index import index_page

from fut_in_pst_typology.urls import fpt_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include([path('', index_page), *pwa_urlpatterns])),
    path('', index_page),
    # path('', include('pwa.urls')),
    
    path('fut-in-pst-typology/', include(fpt_url_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
