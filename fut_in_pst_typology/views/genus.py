from django.shortcuts import render
from django.db.models import Count

from ..models.genus import Genus
from ..models.family import Family
from ..models.language import Language


def genus_page(request):
    cur_genus_name = request.GET.get("name")
    cur_genus_obj = Genus.objects.get(name=cur_genus_name)

    context = {
        "cur_genus": cur_genus_obj,
        "languages": Language.objects.all(),
        "genuses": Genus.objects.all(),
        "families": Family.objects.all(),
        "genus_list": Genus.objects.annotate(language_count=Count('language')),
        "cur_genus_languages": Language.objects.filter(genus=cur_genus_obj.id),
    }
    return render(request, "genus.html", context)
