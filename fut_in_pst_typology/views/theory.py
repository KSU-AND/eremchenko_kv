from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse

from ..models.theory import TheoryBlock
from ..forms.theory_form import TheoryTitleForm, TheoryOutlineForm, TheoryTextForm

def theory_page(request):
    context = {
        "theory_blocks": TheoryBlock.objects.order_by("title").all(),
    }
    return render(request, "theory/home.html", context)

def theory_view_page(request):
    cur_theory_block = TheoryBlock.objects.prefetch_related('languages').get(id=request.GET.get("id"))

    context = {
        "theory_block": cur_theory_block,
        "theory_blocks": TheoryBlock.objects.all(),
    }
    return render(request, "theory/view.html", context)

def theory_edit_page(request):
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

def theory_create(request):
    new_theory_block = TheoryBlock.objects.create(title="Title", 
                                                  outline="<div>outline</div>",
                                                  text="<div>text</div>")
    return redirect(reverse("fpt.theory.edit")+f"?id={new_theory_block.id}")

def theory_delete(request):
    theory_block = TheoryBlock.objects.get(id=request.GET.get("id"))
    theory_block.delete()
    return redirect(reverse("fpt.theory"))