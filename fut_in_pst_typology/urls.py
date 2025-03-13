from django.urls import path, include

from .views import home, summary, statistics, theory, biblio
from .views import language, family, genus, area


theory_url_patterns = [
    path('', theory.TheoryView.as_view(), name="fpt.theory"),
    path('show/<int:id>', theory.TheoryView.Show.as_view(), name="fpt.theory.show"),
    path('edit/<int:id>', theory.TheoryView.Edit.as_view(), name="fpt.theory.edit"),
    path('delete/<int:id>', theory.TheoryView.Delete.as_view(), name="fpt.theory.delete"),
    path('create/', theory.TheoryView.Create.as_view(), name="fpt.theory.create"),
]

fpt_url_patterns = [
    path('', home.HomeView.as_view(), name="fpt"),
    
    path('summary/', summary.SummaryView.as_view(), name="fpt.summary"),
    path('statistics/', statistics.StatisticsView.as_view(), name="fpt.statistics"),
    path('biblio/', biblio.BiblioView.as_view(), name="fpt.biblio"),
    path('theory/', include(theory_url_patterns)),

    path('language/<str:code>', language.LanguageView.as_view(), name="fpt.language"),
    path('area/<int:id>', area.AreaView.as_view(), name="fpt.area"),
    path('genus/<int:id>', genus.GenusView.as_view(), name="fpt.genus"),
    path('family/<int:id>', family.FamilyView.as_view(), name="fpt.family"),
]
