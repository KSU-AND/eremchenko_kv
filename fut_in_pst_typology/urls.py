from django.urls import path

from .views.home import home_page
from .views.theory import theory_page
from .views.theory import theory_view_page, theory_edit_page, theory_create, theory_delete
from .views.statistics import stats_page

from .views.language import language_page
from .views.family import family_page
from .views.genus import genus_page


fpturlpatterns = [
    path('', home_page, name="fpt"),
    path('statistics/', stats_page, name="fpt.statistics"),

    path('theory/', theory_page, name="fpt.theory"),
    path('theory/view/', theory_view_page, name="fpt.theory.view"),
    path('theory/edit/', theory_edit_page, name="fpt.theory.edit"),
    path('theory/create/', theory_create, name="fpt.theory.create"),
    path('theory/delete/', theory_delete, name="fpt.theory.delete"),

    path('summary/', home_page, name="fpt.summary"),
    path('language/', language_page, name="fpt.language"),
    path('family/', family_page, name="fpt.family"),
    path('genus/', genus_page, name="fpt.genus"),
]
