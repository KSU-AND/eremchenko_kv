from django.views import View
from django.shortcuts import render
from django.db.models import Q, Count

from ..models.language import Language


class StatisticsView(View):
    def __init__(self):
        super().__init__()
        self.languages = Language.objects.aggregate(
            total=Count("id"),
            ts=Count("id", filter=~Q(tense_system="")),
            marks_all=Count("id", filter=~Q(fut="") & ~Q(pst="")),
            marks_any=Count("id", filter=~Q(fut="") | ~Q(pst="")),
            combs_all=Count("id", filter=~Q(aa="") & ~Q(am="") & ~Q(ma="") & ~Q(mm="")),
            combs_any=Count("id", filter=~Q(aa="") | ~Q(am="") | ~Q(ma="") | ~Q(mm="")),
            main_comment_all=Count("id", filter=Q(main_comment__contains="\n")),
            main_comment_any=Count("id", filter=~Q(main_comment="")),
    )

    def get(self, request):
        context = {
            "ts": self.construct_context("ts"),
            "marks": self.construct_context("marks_all", "marks_any"),
            "combs": self.construct_context("combs_all", "combs_any"),
            "main_comment": self.construct_context("main_comment_all", "main_comment_any"),
        }

        return render(request, "stats/home.html", context)
    
    def construct_context(self, str_all, str_any=""):
        total = self.languages["total"]
        _all = self.languages[str_all]
        if str_any: _any = self.languages[str_any]

        d = {"all": {"pcnt":(_all) / total * 100, "num": _all}}
        if str_any:
            d["any"] = {"pcnt": (_any - _all) / total * 100, "num": _any - _all}
            d["not"] = {"pcnt": (total - _any) / total * 100, "num": total - _any}
        else:
            d["not"] = {"pcnt": (total - _all) / total * 100, "num": total - _all}
        return d