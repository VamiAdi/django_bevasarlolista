from django.shortcuts import render

# Create your views here.

from .models import Arucikk

def home_view(request, *args, **kwargs):

    if  request.method == "POST":
        if request.POST["formtipus"] == "ujaru":
            Arucikk.hozzaadas(request.POST)
        elif request.POST["formtipus"] == "aruki":
            Arucikk.eltuntetes(request.POST)
    if  request.method =="GET":
        print("GET lekérés történt")
        
    kontextus = {"aru": Arucikk.objects.all()}
    return render(request, "home.html", kontextus)
