from django.shortcuts import render


def index_page(request):
    print(request.user.is_anonymous)
    context = {
        "user": request.user,
    }
    return render(request, "index.html", context)
