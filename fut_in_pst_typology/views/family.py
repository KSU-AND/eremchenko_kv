from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

from ..models.genus import Genus
from ..models.family import Family
from ..models.language import Language


class FamilyView(View):
    def get(self, request, id):
        current_family = Family.objects.get(id=id)
        
        context = {
            "cur_family": current_family,
            "cur_family_languages": Language.objects.select_related("genus").filter(family=current_family),
            
            "languages": Language.objects.order_by("name").all(),
            "genuses": Genus.objects.order_by("name").all(),
            "families": Family.objects.order_by("name").all(),
        }
        return render(request, "family.html", context)
