from django.urls import path

from fut_in_pst_typology.views.home import home_page
from fut_in_pst_typology.views.theory import theory_page
from fut_in_pst_typology.views.theory import theory_view_page, theory_edit_page

from fut_in_pst_typology.views.language import language_page
from fut_in_pst_typology.views.family import family_page
from fut_in_pst_typology.views.genus import genus_page


fpturlpatterns = [
    path('', home_page, name="fpt"),
    path('statistics/', home_page, name="fpt.statistics"),
    path('theory/', theory_page, name="fpt.theory"),
    path('theory/view/', theory_view_page, name="fpt.theory.view"),
    path('theory/edit/', theory_edit_page, name="fpt.theory.edit"),
    path('summary/', home_page, name="fpt.summary"),
    
    path('language/', language_page, name="fpt.language"),
    path('family/', family_page, name="fpt.family"),
    path('genus/', genus_page, name="fpt.genus"),
]
