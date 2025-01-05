from django.shortcuts import render, HttpResponse

from ..models.theory import TheoryBlock
from ..forms.theory_form import TheoryTitleForm, TheoryOutlineForm, TheoryTextForm

def theory_page(request):
    context = {
        "theory_blocks": TheoryBlock.objects.all(),
    }
    return render(request, "theory/home.html", context)

def theory_view_page(request):
    cur_theory_block = TheoryBlock.objects.get(id=request.GET.get("id"))

    context = {
        "theory_block": cur_theory_block,
        "theory_blocks": TheoryBlock.objects.all(),
        "theory_block_languages" : cur_theory_block.languages.all(),
    }
    return render(request, "theory/view.html", context)

def theory_edit_page(request):
    cur_theory_block = TheoryBlock.objects.get(id=request.GET.get("id"))
    
    if request.method == "POST":
        if request.POST.get("title") is not None:
            print(request.POST.get("title"))
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
        "theory_title_form": TheoryTitleForm(instance=cur_theory_block),
        "theory_outline_form": TheoryOutlineForm(instance=cur_theory_block),
        "theory_text_form": TheoryTextForm(instance=cur_theory_block),
    }
    return render(request, "theory/edit.html", context)