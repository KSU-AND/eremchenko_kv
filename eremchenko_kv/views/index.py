from django.shortcuts import redirect
from django.urls import reverse


def index_page(request):
    return redirect(reverse("fpt"))
