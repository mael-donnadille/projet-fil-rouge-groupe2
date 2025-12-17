from django.shortcuts import render

def roles(request):
    return render(request, "core/roles.html")

def carte_page(request):
    return render(request, "core/carte.html")

def conseils_page(request):
    return render(request, "core/conseils.html")
