from django.urls import path, include

from .views import home, summary, statistics, theory
from .views import language, family, genus


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
    path('theory/', include(theory_url_patterns)),

    path('language/<str:code>', language.LanguageView.as_view(), name="fpt.language"),
    path('family/', family.FamilyView.as_view(), name="fpt.family"),
    path('genus/', genus.GenusView.as_view(), name="fpt.genus"),
]
