from email import message
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from attr import fields
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

    # vacunadores = Vacunador.objects.all()
    # data= {
    #     'vacunadores' : vacunadores
    # }
    # administradores = Administrador.objects.all()
    # data= {
    #     'administradores' : administradores
    # }

    return render(request, "main/inicio_admin.html",{"administradores" : administradorList})


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
    return render(request,  "main/eliminar_vacunador.html", context)
