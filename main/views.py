from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador

def homepage(request):
    return render(request, "main/inicio.html", { "vacunadores" : Vacunador.objects.all})

    # a nuestra template le vamos a pasar toda esa cantidad de objteos con la variable vacunadores

def login(request):
    return render(request, "main/inicio_de_sesión.html")

# Create your views here.
