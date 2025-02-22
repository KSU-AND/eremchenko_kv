from django.views import View
from django.shortcuts import render
from django.db.models import Q, Count

from ..models.language import Language


class StatisticsView(View):
    def __init__(self):
        super().__init__()
        self.languages = Language.objects.aggregate(
            DN=Count("id", filter=Q(progress="DN")),
            CH=Count("id", filter=Q(progress="CH")),
            IP=Count("id", filter=Q(progress="IP")),
            NI=Count("id", filter=Q(progress="NI")),
            NL=Count("id", filter=Q(progress="")),
        )

    def get(self, request):
        context = {
            "DN": self.languages["DN"], 
            "CH": self.languages["CH"], 
            "IP": self.languages["IP"], 
            "NI": self.languages["NI"], 
            "NL": self.languages["NL"], 
        }

        return render(request, "stats/home.html", context)
