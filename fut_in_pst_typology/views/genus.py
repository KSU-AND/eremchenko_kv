from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

from ..models.genus import Genus
from ..models.family import Family
from ..models.language import Language


class GenusView(View):
    def get(self, request, id):
        current_genus = Genus.objects.get(id=id)
        
        context = {
            "cur_genus": current_genus,
            "cur_genus_languages": Language.objects.select_related("family").filter(genus=current_genus),
            
            "languages": Language.objects.order_by("name").all(),
            "genuses": Genus.objects.order_by("name").all(),
            "families": Family.objects.order_by("name").all(),
        }
        return render(request, "genus.html", context)
