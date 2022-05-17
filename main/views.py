from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador
from django.contrib.auth.forms import UserCreationForm
def homepage(request):
    return render(request, "main/inicio.html", { "vacunadores" : Vacunador.objects.all})

    # a nuestra template le vamos a pasar toda esa cantidad de objteos con la variable vacunadores

<<<<<<< HEAD
def registro(request):
    form =UserCreationForm
    return render(request, "main/registro.html", {"form":form})
# extenser el formulario para que pida email
=======
def login(request):
    return render(request, "main/inicio_de_sesión.html")

>>>>>>> 8a1dbd2616431fc6a980c63c0c611e31898e16e5
# Create your views here.
