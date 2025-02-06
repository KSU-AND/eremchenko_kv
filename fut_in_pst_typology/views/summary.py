from django.views import View
from django.shortcuts import render

from fut_in_pst_typology.models.language import Language


class SummaryView(View):
    def get(self, request):
        context = {
            "languages": Language.objects.select_related("genus", "family").order_by("name").all(),
        }
        return render(request, "summary.html", context)