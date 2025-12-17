from django.shortcuts import render

def roles(request):
    return render(request, "core/roles.html")

def carte(request):
    return render(request, "core/carte.html")

def conseils(request):
    return render(request, "core/conseils.html")

