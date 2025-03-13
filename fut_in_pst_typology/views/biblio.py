from django.views import View
from django.shortcuts import render
from django.db.models import Q, Count

from ..models.source import Source


class BiblioView(View):
    def __init__(self):
        super().__init__()
        self.sources = Source.objects.select_related("lang").order_by("source").all()

    def get(self, request):
        context = {
            "sources": self.sources, 
        }

        return render(request, "biblio/home.html", context)
