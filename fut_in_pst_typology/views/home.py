from django.shortcuts import render

from fut_in_pst_typology.models.language import Language


def home_page(request):
    context = {
        "languages": Language.objects.all(),
    }
    return render(request, "home.html", context)
