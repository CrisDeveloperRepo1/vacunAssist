from email import message
from random import random
from certifi import contents
import django
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from attr import fields
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib.style import context
from .models import Vacunador, Envio_de_correo, Administrador,Vacunatorio
from django.contrib.auth.forms import UserCreationForm
from .forms import vacunador_signUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import logout, authenticate

def sumarTotales(request):
    VacunatorioList= Vacunatorio.objects.all()
    totalVFA = 0
    totalVG= 0
    totalVC= 0
    for v in VacunatorioList:
        totalVFA = totalVFA + v.stock_vac_fa
    for v in VacunatorioList:
        totalVG = totalVG + v.stock_vac_gripe
    for v in VacunatorioList:
        totalVC = totalVC + v.stock_vac_covid
        #,{"total":totalVFA}
    return render(request,"main/pruebas.html",{"vacunasFA":totalVFA,"vacunasG":totalVG,"vacunasC":totalVC,"Vacunatorios":VacunatorioList})

def actualizar_stock (request):
    return render(request, "main/actualizar.html")


def homepage(request):
    return render(request, "main/inicio.html", { "vacunadores" : Vacunador.objects.all})

    # a nuestra template le vamos a pasar toda esa cantidad de objteos con la variable vacunadores

def listarModelos(request):
    return render(request,"main/pruebas.html")


def registro(request):
    form =UserCreationForm
    return render(request, "main/registro.html", {"form":form})
# extenser el formulario para que pida email


def login(request):
    return render(request, "main/inicio_de_sesión.html")


def verif(request):
    return render(request,"main/verif.html")

def inicio_admin(request):

    administradorList= Administrador.objects.all()
    vacunadorList= Vacunador.objects.all()

    # vacunadores = Vacunador.objects.all()
    # data= {
    #     'vacunadores' : vacunadores
    # }
    # administradores = Administrador.objects.all()
    # data= {
    #     'administradores' : administradores
    # }

    return render(request, "main/inicio_admin.html",{"administradores" : administradorList, "vacunadores" : vacunadorList})


    vacunadores = Vacunador.objects.all()
    data= {
        'vacunadores' : vacunadores
    }
    administradores = Administrador.objects.all()
    data= {
        'administradores' : administradores
    }

    return render(request, "main/inicio_admin.html", data)



# def validarCodigo(request):
#
#     return render(request, "main/validarCodigo.html",{"administrador": Administrador.objects.all})

def validarUsuario(request):

    if request.GET["dni"].isdigit():
        # one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])

        try:
            # blog = Blog.objects.get(id=1)
            # entry = Entry.objects.get(blog=blog, entry_number=1)
            one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])
            if request.GET["pass"].isdigit():
                if  int(request.GET["pass"]) == one_entry.administrador_contraseña :
                     return render(request,"main/verif.html")
                else:
                    messages.error(request, " la contraseña es ingresada es invalida")
                    return render(request,"main/inicio_de_sesión.html")
            else:
                if  request.GET["pass"] == one_entry.administrador_contraseña :
                     return render(request,"main/verif.html")
                else:
                    messages.error(request, " la contraseña es ingresada es invalida")
                    return render(request,"main/inicio_de_sesión.html")

        except ObjectDoesNotExist:
           print("Either the blog or entry doesn't exist.")
           messages.error(request, " el dni ingresado no pertenece a un usuario del sistema")
           return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina
    else:
        messages.error(request, "el dni ingresado debe contener numeros")
        return render(request,"main/inicio_de_sesión.html")






def compararCodigo(request):
        administradorList= Administrador.objects.all()
        vacunadoresList= Vacunador.objects.all()
    # codigo=request.GET{"pass"}
    # if check_password(codigo,administrador. ) // falta la instancia
        if request.GET["pass"]:
                    if request.GET["pass"].isdigit():
                                one_entry = Administrador.objects.get(administrador_nombre="Lautaro")
                                if  int(request.GET["pass"]) == one_entry.administrador_codigo :
                                    #mensaje= request.GET["pass"]

                                    return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
                                else:
                                    messages.error(request, "codigo invalido")
                                    return render (request,"main/verif.html")

                    else:
                        messages.error(request, "debe ingresar numeros")
                        return render (request,"main/verif.html")




        else:
            messages.error(request, "no ingreso nada")
            return render (request,"main/verif.html")



        # if request.GET["pass"].isdigit():
                    # if  int(request.GET["pass"]) == one_entry.administrador_contraseña :
                    #     mensaje= request.GET["pass"]
                    #
                    #     return render(request,"main/inicio_admin.html")
            # return render(request,"main/inicio_admin.html")

        # codigo = int(request.GET["pass"])
        # if type(request.GET["pass"]) == int :
        #
        #     return render(request,"main/inicio_admin.html")
        #
        # if type:
        #     messages.error(request, "debe ingresar un numero")
        #     return render (request,"main/validarCodigo.html")



        # if  int(request.GET["pass"]) == one_entry.administrador_contraseña :
        #     mensaje= request.GET["pass"]
        #
        #     return render(request,"main/inicio_admin.html")
        # else:
        # messages.error(request, "debe ingresar un numero solamente")
        # return render (request,"main/validarCodigo.html")






        # messages.error(request, "no ha ingresado nada")
        #
        #
        #
        # mensaje="no has introducido nada"
        # # messages.success(request,"nueva")
        #
        # return render (request,"main/validarCodigo.html")

    # return render(request, "main/inicio.html"  )


def recup_contra(request):
    return render(request, "main/recuperar-contraseña.html")

def send_email_registro(mail):
    context = {"mail" : mail }
    template = get_template("main/correo.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Registro en VacunAssist ", 
        "registro de usuarios",
        settings.EMAIL_HOST_USER,
        [mail]        
    )
    
    email.attach_alternative(content, "text/html")
    email.send()


def reg_vac(request):

    #data = {
    #    "form": vacunador_signUpForm()}
    #if request.method == "POST":
     #    formulario = UserCreationForm(request.POST)
      #   if formulario.is_valid():
     #       user = formulario.save()
            
     #       dni = form.cleaned_data["dni"]
     #       user = authenticate(dni=dni)
     #       login(request, user)
     #       return redirect(to="login")

    form= vacunador_signUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
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
        if request.method == "POST":
            mail = request.POST.get("mail")
            caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
            longitud = 9  # La longitud que queremos
            contraseña = ''.join(choice(caracteres) for caracter in range(longitud))

        send_email_registro(mail)
    context={
        'form': form,
    }
    return render(request, "main/inicio_admin.html", context)

    #class reg_vac(View):

    #def get(self, request):
    #    form = UserCreationForm()
    #    return render(request, "main/inicio_admin.html", {"form": form})

    #def post(self, request):
     #   form = UserCreationForm(request.POST)
     #   if form.is_valid():
     #       user = form.save()
     #       dni_user = form.cleaned_data.get("dni")
     #       messages.success(request, F"Se ha registrado con exito {dni_user}")
     #       login(request, user)
     #       return redirect("main/login")
     #   else:
     #       for msg in form.error_messages:
     #           messages.error(request, form.error_messages[msg])

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
    return render(request,  "main/eliminar_vacunador.html", context)

def cerrar_sesion (request):
    request.session.flush()
    messages.success(request, "Tu sesión se cerró correctamente")
    return redirect('main/login/')

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings



def send_email(mail, contraseña):
    context = {"mail" : mail,
               "pass" : contraseña
               }
    template = get_template("main/correo.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Recuperar contraseña ", 
        "probando envio de mails en django",
        settings.EMAIL_HOST_USER,
        [mail]        
    )
    
    email.attach_alternative(content, "text/html")
    email.send()

from secrets import choice

def index(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        longitud = 6  # La longitud que queremos
        contraseña = ''.join(choice(caracteres) for caracter in range(longitud))

        send_email(mail, contraseña)
        
    return render(request, "main/index.html", {})


def reset_pass(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        longitud = 9  # La longitud que queremos
        contraseña = ''.join(choice(caracteres) for caracter in range(longitud))

        send_email(mail, contraseña)
        
    return render(request, "main/recuperar-contraseña.html", {})


