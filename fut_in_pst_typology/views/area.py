from django.views import View
from django.shortcuts import render

from ..models.area import Area
from ..models.genus import Genus
from ..models.family import Family
from ..models.language import Language


class AreaView(View):
    def get(self, request, id):
        current_area = Area.objects.get(id=id)
        
        context = {
            "cur_area": current_area,
            "cur_area_languages": Language.objects.select_related("family", "genus").filter(area=current_area),
            
            "languages": Language.objects.order_by("name").all(),
            "areas": Area.objects.order_by("name").all(),
            "genuses": Genus.objects.order_by("name").all(),
            "families": Family.objects.order_by("name").all(),
        }
        return render(request, "area.html", context)
