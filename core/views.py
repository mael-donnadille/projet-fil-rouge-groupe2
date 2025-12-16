from django.shortcuts import render

def lee_sin_view(request):
    return render(request, "core/lee_sin.html")
