from django.shortcuts import render
from django.db.models import Q, F, Count

from ..models.language import Language

def construct_dict(l, str_all, str_any=""):
    total = l["total"]
    _all = l[str_all]
    if str_any: _any = l[str_any]

    d ={"all": {"pcnt":(_all) / total * 100, "num": _all}}
    if str_any:
        d["any"] = {"pcnt": (_any - _all) / total * 100, "num": _any - _all}
        d["not"] = {"pcnt": (total - _any) / total * 100, "num": total - _any}
    else:
        d["not"] = {"pcnt": (total - _all) / total * 100, "num": total - _all}
    return d

def stats_page(request):
    langs = Language.objects.aggregate(
        total=Count("id"),
        ts=Count("id", filter=~Q(tense_system="")),
        marks_all=Count("id", filter=~Q(fut="") & ~Q(pst="")),
        marks_any=Count("id", filter=~Q(fut="") | ~Q(pst="")),
        combs_all=Count("id", filter=~Q(aa="") & ~Q(am="") & ~Q(ma="") & ~Q(mm="")),
        combs_any=Count("id", filter=~Q(aa="") | ~Q(am="") | ~Q(ma="") | ~Q(mm="")),
        main_comment_all=Count("id", filter=Q(main_comment__contains="\n")),
        main_comment_any=Count("id", filter=~Q(main_comment="")),
    )
    
    context = {
        "ts": construct_dict(langs, "ts"),
        "marks": construct_dict(langs, "marks_all", "marks_any"),
        "combs": construct_dict(langs, "combs_all", "combs_any"),
        "main_comment": construct_dict(langs, "main_comment_all", "main_comment_any"),
    }
    return render(request, "stats/home.html", context)
