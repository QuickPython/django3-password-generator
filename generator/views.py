from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, "generator/index.html")

def about(request):
    return render(request, "generator/about.html")

def password(request):

    characters = list("acdefghijklmnopqrstuvxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVXYZ"))

    if request.GET.get("special"):
        characters.extend(list("!'#$%&/()=?*-_"))

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    length = int(request.GET.get("length", 12))

    the_password = ""

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": the_password})
