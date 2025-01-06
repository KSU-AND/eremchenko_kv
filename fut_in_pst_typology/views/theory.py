from django.shortcuts import render, HttpResponse

from ..models.theory import TheoryBlock
from ..models.language import Language
from ..forms.theory_form import TheoryTitleForm, TheoryOutlineForm, TheoryTextForm, LanguageForm

def theory_page(request):
    context = {
        "theory_blocks": TheoryBlock.objects.all(),
    }
    return render(request, "theory/home.html", context)

def theory_view_page(request):
    cur_theory_block = TheoryBlock.objects.prefetch_related('languages').get(id=request.GET.get("id"))

    if request.method == "POST":
        if request.POST.get("languages") is not None:
            language = Language.objects.get(id=request.POST.get("languages"))
            # if not language in cur_theory_block.languages.all():
                # languages = list(cur_theory_block.languages.all())
                # languages.append(language)
            languages_form = LanguageForm(request.POST, instance=cur_theory_block)
            languages_form.save()
            # return HttpResponse(status=200)

    context = {
        "theory_block": cur_theory_block,
        "theory_blocks": TheoryBlock.objects.all(),
        "forms": {"languages": LanguageForm(instance=cur_theory_block),}
    }
    return render(request, "theory/view.html", context)

def theory_edit_page(request):
    cur_theory_block = None
    if "create" in request.META.get('PATH_INFO', None):
        cur_theory_block = TheoryBlock.objects.create()
    else:
        cur_theory_block = TheoryBlock.objects.get(id=request.GET.get("id"))
    
    if request.method == "POST":
        if request.POST.get("title") is not None:
            title_form = TheoryTitleForm(request.POST, instance=cur_theory_block)
            title_form.save()
            return HttpResponse(status=200)
        if request.POST.get("outline") is not None:
            outline_form = TheoryOutlineForm(request.POST, instance=cur_theory_block)
            outline_form.save()
            return HttpResponse(status=200)
        if request.POST.get("text") is not None:
            text_form = TheoryTextForm(request.POST, instance=cur_theory_block)
            text_form.save()
            return HttpResponse(status=200)

    context = {
        "theory_block": cur_theory_block,
        "theory_blocks": TheoryBlock.objects.all(),
        "forms": {"title": TheoryTitleForm(instance=cur_theory_block),
                  "outline": TheoryOutlineForm(instance=cur_theory_block),
                  "text": TheoryTextForm(instance=cur_theory_block),
        }
    }
    return render(request, "theory/edit.html", context)
