from django.shortcuts import render

from fut_in_pst_typology.models.language import Language


def summary_page(request):
    context = {
        "languages": Language.objects.select_related("genus", "family").all(),
    }
    return render(request, "summary.html", context)
