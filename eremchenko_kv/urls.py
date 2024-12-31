from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from eremchenko_kv import settings
from eremchenko_kv.views.index import index_page
from fut_in_pst_typology.views.home import home_page
from fut_in_pst_typology.views.language import language_page
from fut_in_pst_typology.views.family import family_page
from fut_in_pst_typology.views.genus import genus_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    
    path('fut-in-pst-typology/', home_page, name="fpt"),
    path('fut-in-pst-typology/statistics', home_page, name="fpt.statistics"),
    path('fut-in-pst-typology/theory', home_page, name="fpt.theory"),
    path('fut-in-pst-typology/summary/', home_page, name="fpt.summary"),
    
    path('fut-in-pst-typology/language/', language_page, name="fpt.language"),
    path('fut-in-pst-typology/family/', family_page, name="fpt.family"),
    path('fut-in-pst-typology/genus/', genus_page, name="fpt.genus"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
