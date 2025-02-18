from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from eremchenko_kv import settings
from eremchenko_kv.views.index import index_page

from fut_in_pst_typology.urls import fpt_url_patterns
from accounts.urls import accounts_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    
    path('fut-in-pst-typology/', include(fpt_url_patterns)),
    path('accounts/', include(accounts_url_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
