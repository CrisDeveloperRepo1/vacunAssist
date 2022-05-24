from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador
from .models import Administrador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
def homepage(request):
    return render(request, "main/inicio.html", { "vacunadores" : Vacunador.objects.all})

    # a nuestra template le vamos a pasar toda esa cantidad de objteos con la variable vacunadores




def registro(request):
    form =UserCreationForm
    return render(request, "main/registro.html", {"form":form})
# extenser el formulario para que pida email


def login(request):
    return render(request, "main/inicio_de_sesión.html")


def login(request):
    return render(request, "main/inicio_de_sesión.html")

def verificar(request):
    return render(request, "main/verificación.html")

def inicio_adm(request):
    return render(request, "main/inicio-admin.html")

def validarCodigo(request):

    return render(request, "main/validarCodigo.html",{"administrador": Administrador.objects.all})

def compararCodigo(request):
    codigo=request.GET{"pass"}
    if check_password(codigo,administrador. ) // falta la instancia

    return render(request, "main/inicio_de_sesión.html"  )

# Create your views here.
