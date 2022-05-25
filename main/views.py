from email import message
from django.contrib import messages
from attr import fields
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador, Envio_de_correo, Administrador
from django.contrib.auth.forms import UserCreationForm
from .forms import vacunador_signUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



def homepage(request):
    return render(request, "main/inicio.html", { "vacunadores" : Vacunador.objects.all})

    # a nuestra template le vamos a pasar toda esa cantidad de objteos con la variable vacunadores




def registro(request):
    form =UserCreationForm
    return render(request, "main/registro.html", {"form":form})
# extenser el formulario para que pida email


def login(request):
    return render(request, "main/inicio_de_sesión.html")


def verificar(request):
    return render(request, "main/verificación.html")

def inicio_adm(request):
    return render(request, "main/inicio-admin.html")


def validarCodigo(request):

    return render(request, "main/validarCodigo.html",{"administrador": Administrador.objects.all})

def compararCodigo(request):
    # codigo=request.GET{"pass"}
    # if check_password(codigo,administrador. ) // falta la instancia

    return render(request, "main/inicio_de_sesión.html"  )


def recup_contra(request):
    return render(request, "main/recuperar-contraseña.html")

def reg_vac(request):
    
    form= vacunador_signUpForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if Vacunador.objects.filter(dni= instance.vacunador_dni).exists():
            messages.Warning(request, "El DNI ya existe")
        else:
            instance.save()
            messages.success(request, "Enviamos un correro electronico a " + instance.vacunador_email)
            #correo electronico
            
            subject="Registro de Vacunador"
            from_email= settings.EMAIL_HOST_USER
            to_email=[instance.vacunador_email]
            
            html_template="email_templates/welcome.html"
            html_message=render_to_string(html_template)
            message=EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype="html"
            message.send()
    context={
        'form': form,
    }
    return render(request, "main/registro_vacunador.html", context)

# Create your views here.
def eliminar_vacunador(request):
    form= vacunador_signUpForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if Vacunador.objects.filter(dni= instance.vacunador_dni).exists():
            Vacunador.objects.filter(dni= instance.vacunador_dni).delete()
            messages(request, "El usuario con dni " + instance.vacunador_dni + " se eliminó correctamente")
        else:
            print("el dni no existe")
            messages.Warning(request, "el dni no existe")
    context={
        'form': form,
    }
    return render(request, "main/eliminar_vacunador.html", context)
