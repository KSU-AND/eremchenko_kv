from django.views import View
from django.shortcuts import render

from fut_in_pst_typology.models.language import Language


class AnalysisView(View):
    def get(self, request):
        context = {
            "languages": Language.get_yes_languages(),
        }
        return render(request, "analysis/home.html", context)