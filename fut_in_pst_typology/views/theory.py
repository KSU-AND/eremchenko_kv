from django.shortcuts import render

from fut_in_pst_typology.models.theory import TheoryBlock


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
    }
    return render(request, "theory/view.html", context)