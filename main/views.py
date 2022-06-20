from email import message
from random import random
#from certifi import contents
import django
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from attr import fields
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from matplotlib.style import context
from .models import Vacunador, Envio_de_correo, Administrador,Vacunatorio
from django.contrib.auth.forms import UserCreationForm
from .forms import vacunador_signUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from email import message
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
# from attr import fields
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador, Envio_de_correo, Administrador,Vacunatorio,Vacuna_Fiebre_Am,Vacuna_Covid,Paciente,SolicitudTurnoFA,Logeado,TurnoFAAprobados
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import vacunador_signUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate,logout
from.forms import CustomUserForm
from.forms import VacunadorRegistro,PacienteRegistro,vacunador_signUpForm
import math, random
from datetime import datetime
from datetime import datetime
from datetime import date

# def inicio_admin(request):
#     # data2= {
#     #   'form' :PacienteRegistro()
#     # }
#     # if request.method == 'POST':
#     #     formulario = PacienteRegistro(request.POST)
#     #     if formulario.is_valid():
#     #         formulario.save()
#     administradorList= Administrador.objects.all()
#
#     # vacunadores = Vacunador.objects.all()
#     # data= {
#     #     'vacunadores' : vacunadores
#     # }
#     # administradores = Administrador.objects.all()
#     # data= {
#     #     'administradores' : administradores
#     # }
#
#     return render(request, "main/inicio_admin.html",{"administradores" : administradorList})
#
#
#     vacunadores = Vacunador.objects.all()
#     data= {
#         'vacunadores' : vacunadores
#     }
#     administradores = Administrador.objects.all()
#     data= {
#         'administradores' : administradores
#     }
#
#
#
#
#     return render(request, "main/inicio_admin.html", data)

def cancelarTurno (request):
#### agregar metodo q devuelva el ultimo objeto de la tabla
    usuario = Logeado.objects.get(numId=3)
    TurnoFA= TurnoFAAprobados.objects.get(dni=usuario.usuarioLogeado)
    TurnoFA.delete()
    paciente= Paciente.objects.get(paciente_dni=usuario.usuarioLogeado)
    paciente.vac_Amarilla_turno= None
    paciente.save()
    return render(request,"main/inicioPaciente.html",{"valor":2,"p":paciente})

def evaluarTurno(request):
    ListSolicitud= SolicitudTurnoFA.objects.all()

    return render(request,"main/evaluarTurnos.html",{"turnos":ListSolicitud})

########## SOLICITUD DE TURNO DE FIEBRE AMARILLA ###############################################################
def solicitarTurnoFA(request):
        one = Logeado.objects.get(numId=3)

        one_entry = Paciente.objects.get(paciente_dni=one.usuarioLogeado)
        # usuarioLogeado=models.IntegerField()
        # numId=models.IntegerField()
        Dni=one_entry.paciente_dni
        NumId=0
        #23242424
        # inicio = datetime(2022, 6, 30)
        # final =  datetime(2022, 9, 28)
        # random_date = inicio + (final - inicio) * random.random()
        # one_entry.vac_Amarilla_turno=random_date
        # one_entry.save()
        today = date.today()

        age = today.year - one_entry.paciente_fechaNac.year - ((today.month, today.day) < (one_entry.paciente_fechaNac.month, one_entry.paciente_fechaNac.day))
        #
        # age = today.year - self.fecha_nac.year - (
        #             (today.month, today.day) < (self.fecha_nac.month, self.fecha_nac.day))
        print(age)


        #edad = relativedelta(datetime.now(), datetime(1988, 4, 15))
        Email=one_entry.paciente_email
        turno=SolicitudTurnoFA.objects.create(dni=Dni,numId=NumId,email=Email,edad=age)
        messages.error(request, "solicitud exitosa")
        return render(request,"main/inicioPaciente.html",{"valor":1,"p":one_entry})

def inicioPaciente(request):

    one = Logeado.objects.get(numId=3)


    one_entry = Paciente.objects.get(paciente_dni=one.usuarioLogeado)
    today = date.today()

    age = today.year - one_entry.paciente_fechaNac.year - ((today.month, today.day) < (one_entry.paciente_fechaNac.month, one_entry.paciente_fechaNac.day))
    if (age >= 60):
        return render(request, "main/inicioPaciente.html",{"valor":3, "p":one_entry})

    else:

###########################################
        try:


            one1 = SolicitudTurnoFA.objects.get(dni=one_entry.paciente_dni)


            return render(request, "main/inicioPaciente.html",{"valor":1, "p":one_entry})

                # dni=models.IntegerField()
                # numId=models.IntegerField()
                # email= models.EmailField(max_length=254

        except ObjectDoesNotExist:
            return render(request, "main/inicioPaciente.html",{"valor":2,"p":one_entry})
###############################################
    # f='f'
    # OTP=''
    # OTP=2332
    #
    # return render(request, "main/inicioPaciente.html",{"codigo": OTP})
############ REGISTRO DE PACIENTE ##########################################################
def registrarPaciente(request):
    return render(request, "main/registrarPaciente.html")
def registroPaciente(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    fecha=request.POST['fechaesperada']
    dni=request.POST['dni']
    email=request.POST['email']
    zona=request.POST['zona']
    Contraseña=request.POST['Contraseña']
    inicio = datetime(2022, 6, 30)
    final =  datetime(2022, 9, 28)

    # random_date = inicio + (final - inicio) * random.random()
    # vacFaTurno = random_date
    random_turnoCovid = inicio + (final - inicio) * random.random()
    random_gripe = inicio + (final - inicio) * random.random()
    #vac_Gripe_turno=random_gripe
    #vac_Covid_turno1= random_turnoCovid
    #vac_Covid_turno2
    #vac_Amarilla_turno= models.DateTimeField(null=True)

    #print(random_date)


########## GENERO EL CODIGO DE 4 DIGITOS #################################################

    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    codigo=OTP


    digitos = '0123456789'
    longitud = 4  # La longitud que queremos
    codigo = ''.join(choice(digitos) for digito in range(longitud))


    paciente=Paciente.objects.create(codigo=codigo,contraseña=Contraseña,paciente_nombre=nombre,paciente_apellido=apellido,paciente_fechaNac=fecha,paciente_zona=zona,paciente_dni=dni,paciente_email=email,vac_Gripe_turno=random_gripe,vac_Covid_turno1= random_turnoCovid)
    messages.error(request, " PACIENTE REGISTRADO")


########## PASO EL CODIGO EN LA VARIABLE CODIGO  PARA PODER IMPRIMIRLO EN EN CODIGO HTML #############
    ##########send_email_registro(email, codigo, dni, nombre )
    return render(request,'main/registrarPaciente.html',{'codigo': codigo})
    return render(request, "main/registrarPaciente.html",{"codigo" : 3})

###################### empezar Asignacion del turno FA
def empezarAsignacionTurno (request,dni):
    ListSolicitud= SolicitudTurnoFA.objects.all()

    return render(request, "main/evaluarTurnos.html",{"turnos":ListSolicitud,"valor":1,"asignacionDNI":dni})
################### Asignar turno FA
def AsignarTurno (request):
    ListSolicitud= SolicitudTurnoFA.objects.all()
    fecha = request.POST['fechaesperada']
    DNI =request.POST['dni']
    #one_entry=Paciente.objects.get(paciente_dni=request.POST['dni'])
    # Email=one_entry.paciente_email
    # one_entry.vac_Amarilla_turno=fecha
    # one_entry.save()
    # Turno=TurnoFAAprobados.objects.create(dni=DNI,numId=0,email=Email)
    return render(request, "main/evaluarTurnos.html",{"turnos":ListSolicitud,"asignacionDNI":DNI})

############## elimar solicitud de vacuna fiebre amarilla

def eliminarSolicitud (request,dni):
    ListSolicitud= SolicitudTurnoFA.objects.all()
    turno=SolicitudTurnoFA.objects.get(dni=dni)
    turno.delete()
    return render(request, "main/evaluarTurnos.html",{"turnos":ListSolicitud})



def eliminar_Admin(request,id,nombre):

    admin=Vacunador.objects.get(vacunador_dni=id)
    admin.delete()
    #return render(request,'main/eliminarVacunador.html')
    administradorList= Vacunador.objects.all()
    return render(request, "main/eliminarVacunador.html",{"administradores" : administradorList})

def register(request,data2):

    data2= {
      'form' :PacienteRegistro()
    }
    if request.method == 'POST':
        formulario = PacienteRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            #one_entry = User.objects.get(password1="adminadmin")
            #usuario_administrador
            return render(request,"main/inicio.html")

    #     form = UserCreationForm(request.POST)
    #     form.save()
    #
    #     if form.is_valid():
    #         return redirect('/login/')
    # else:
    #     form = UserCreationForm(request.POST)
    # context = { 'form' : form}
    return render(request,'main/registro_Admin.html',data2)

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

def loginAdmin(request):
    try:
        one_entry = Logeado.objects.get(numId=1)

    except ObjectDoesNotExist:
        UsuarioLogeado=0
        NumId=1
        usuario=Logeado.objects.create(usuarioLogeado=UsuarioLogeado,numId=NumId)


    return render(request, "main/inicio_de_sesión.html")
def loginVacunador(request):
    try:
        one_entry = Logeado.objects.get(numId=2)

    except ObjectDoesNotExist:
        UsuarioLogeado=0
        NumId=2
        usuario=Logeado.objects.create(usuarioLogeado=UsuarioLogeado,numId=NumId)

    return render(request, "main/inicio_de_sesión.html")
def loginPaciente(request):
    try:
        one_entry = Logeado.objects.get(numId=3)

    except ObjectDoesNotExist:

        digits = "0123456789"
        OTP = ""

        for i in range(6) :
            OTP += digits[math.floor(random.random() * 10)]
        UsuarioLogeado=0
        NumId=3
        usuario=Logeado.objects.create(usuarioLogeado=UsuarioLogeado,numId=NumId)

    return render(request, "main/inicio_de_sesión.html",{"codigo" : 3})
def main(request):
    records=Logeado.objects.all()
    records.delete()
    return render(request,"main/main.html")
def login1(request):
    records=Logeado.objects.all()
    records.delete()
    return render(request, "main/inicio_de_sesión.html")

def editarStockVacunatorio(request):
    administradorList= Vacunatorio.objects.all()
    VacunaFiebreAm= Vacuna_Fiebre_Am.objects.all()
    VacunaCovid=Vacuna_Covid.objects.all()


    return render(request, "main/editarStockVacunatorio.html",{"administradores" : administradorList,"vacunafa" : VacunaFiebreAm, "vacunaC" : VacunaCovid})

def eliminarVacunador(request):
    administradorList= Vacunador.objects.all()
    return render(request, "main/eliminarVacunador.html",{"administradores" : administradorList})

    #return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})


def verif(request):
    return render(request,"main/verif.html")

def inicio_admin(request):
    data2= {
      'form' :PacienteRegistro()
    }
    administradorList= Administrador.objects.all()

    vacunadoresList= Vacunador.objects.all()

    # data2= {
    #   'form' :PacienteRegistro()
    # }
    # if request.method == 'POST':
    #     formulario = PacienteRegistro(request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #administradorList= Administrador.objects.all()

    vacunadorList= Vacunador.objects.all()


    # vacunadores = Vacunador.objects.all()
    # data= {
    #     'vacunadores' : vacunadores
    # }
    # administradores = Administrador.objects.all()
    # data= {
    #     'administradores' : administradores
    # }


    # return render(request, "main/inicio_admin.html",{"administradores" : administradorList})
    #
    #
    # vacunadores = Vacunador.objects.all()
    # data= {
    #     'vacunadores' : vacunadores
    # }
    # administradores = Administrador.objects.all()
    # data= {
    #     'administradores' : administradores
    # }
    ##return redirect('register', data2)
    ##return redirect('main/registro_Admin.html')
    return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
    #return render(request,'main/registro_Admin.html')

    return render(request, "main/inicio_admin.html",{"administradores" : administradorList, "vacunadores" : vacunadorList})


    #return render(request, "main/inicio_admin.html")



# def validarCodigo(request):
#
#     return render(request, "main/validarCodigo.html",{"administrador": Administrador.objects.all})

### validar usuario para un paciente  ####






def validarUsuario(request):

    if request.GET["dni"].isdigit():
        # one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])

        try:
            q1 = Logeado.objects.get(numId=1)
            q1.usuarioLogeado=request.GET["dni"]
            q1.save()
            try:
                    one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])
                    contraseña= one_entry.contraseña

            except ObjectDoesNotExist:

                    messages.error(request, "  no pertenece a un usuario admin del sistema")
                    return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina

        except ObjectDoesNotExist:
            try:

                q1 = Logeado.objects.get(numId=2)
                q1.usuarioLogeado=request.GET["dni"]
                q1.save()
                try:
                    #one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])
                    one_entry = Vacunador.objects.get(vacunador_dni = request.GET["dni"])
                    contraseña= one_entry.contraseña
                except ObjectDoesNotExist:

                    messages.error(request, "  no pertenece a un usuario vacunador del sistema")
                    return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina

            except ObjectDoesNotExist:

                try:
                   q1 = Logeado.objects.get(numId=3)
                   q1.usuarioLogeado=request.GET["dni"]
                   q1.save()
                   one_entry = Paciente.objects.get(paciente_dni = request.GET["dni"])
                   contraseña= one_entry.contraseña
                   print(request.GET["dni"])
                   # try:
                   #    one_entry = Paciente.objects.get(paciente_dni = request.GET["dni"])
                   #    contraseña= one_entry.contraseña
                   #
                   # except ObjectDoesNotExist:
                   #
                   #     messages.error(request, "  no pertenece a un usuario paciente del sistema")
                   #     return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina
                except ObjectDoesNotExist:
                    print('')
                    messages.error(request, "  no pertenece a un usuario paciente del sistemappppxxx")
                    return render(request,"main/inicio_de_sesión.html",{"codigo" : 3}) # vuelvo a la pagina
#####

####
        try:

            # blog = Blog.objects.get(id=1)
            # entry = Entry.objects.get(blog=blog, entry_number=1)
            #one_entry = Administrador.objects.get(administrador_dni = request.GET["dni"])

            #if request.GET["pass"].isdigit():
                # if  int(request.GET["pass"]) == contraseña :
                #      #login(request, one_entry)
                #      username = request.GET["dni"]
                #      password = request.GET["pass"]
                #      user = authenticate(request, username=username, password=password)
                #      #login(request)
                #      return render(request,"main/verif.html")
                # else:
                #     messages.error(request, " la contraseña es ingresada es invalida")
                #     return render(request,"main/inicio_de_sesión.html")
            #if:
            if  request.GET["pass"] == one_entry.contraseña :
                 return render(request,"main/verif.html")
            else:
                messages.error(request, " la contraseña es ingresada es invalida")
                return render(request,"main/inicio_de_sesión.html")

        except ObjectDoesNotExist:
           print("Either the blog or entry doesn't exist.")
           messages.error(request, " el dni ingresado no pertenece a un usuario del sistemasssssx")
           return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina
    else:
        messages.error(request, "el dni ingresado debe contener numeros")
        return render(request,"main/inicio_de_sesión.html")


### comparar codigo pára usuario paciente
# def compararCodigoPaciente(request):
#         data2= {
#           'form' :PacienteRegistro()
#         }
#         administradorList= Administrador.objects.all()
#         vacunadoresList= Vacunador.objects.all()
#     # codigo=request.GET{"pass"}
#     # if check_password(codigo,administrador. ) // falta la instancia
#         if request.GET["pass"]:
#                     if request.GET["pass"].isdigit():
#                                 #one_entry = Administrador.objects.get(administrador_nombre="Lautaro")
#                                 try:
#                                     one=Logeado.objects.get(numId=1)
#                                     one_entry = Administrador.objects.get(administrador_dni=one.usuarioLogeado)
#                                 except ObjectDoesNotExist:
#                                     try:
#
#                                         one=Logeado.objects.get(numId=2)
#                                         one_entry = Vacunador.objects.get(vacunador_dni=one.usuarioLogeado)
#                                     except ObjectDoesNotExist:
#
#                                         one=Logeado.objects.get(numId=3)
#                                         one_entry = Paciente.objects.get(paciente_dni=one.usuarioLogeado)
#
#                                 if  int(request.GET["pass"]) == one_entry.codigo :
#                                     #mensaje= request.GET["pass"]
#
#                                     return render(request,"main/inicioPaciente.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
#                                 else:
#                                     messages.error(request, "codigo invalido")
#                                     return render (request,"main/verif.html")
#
#                     else:
#                         messages.error(request, "debe ingresar numeros")
#                         return render (request,"main/verif.html")
#
#
#
#
#         else:
#             messages.error(request, "no ingreso nada")
#             return render (request,"main/verif.html")



def compararCodigo(request):
        data2= {
          'form' :PacienteRegistro()
        }
        administradorList= Administrador.objects.all()
        vacunadoresList= Vacunador.objects.all()
    # codigo=request.GET{"pass"}
    # if check_password(codigo,administrador. ) // falta la instancia
        if request.GET["pass"]:
                    if request.GET["pass"].isdigit():
                                #one_entry = Administrador.objects.get(administrador_nombre="Lautaro")

                                try:
                                    one=Logeado.objects.get(numId=1)
                                    one_entry = Administrador.objects.get(administrador_dni=one.usuarioLogeado)
                                    if  int(request.GET["pass"]) == one_entry.codigo :

                                    #mensaje= request.GET["pass"]

                                        return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
                                    else:

                                        messages.error(request, "codigo invalido")
                                        return render (request,"main/verif.html")


                                except ObjectDoesNotExist:
                                    try:

                                        one=Logeado.objects.get(numId=2)
                                        one_entry = Vacunador.objects.get(vacunador_dni=one.usuarioLogeado)
                                        if  int(request.GET["pass"]) == one_entry.codigo :

                                        #mensaje= request.GET["pass"]

                                            return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
                                        else:

                                            messages.error(request, "codigo invalido")
                                            return render (request,"main/verif.html")
                                    except ObjectDoesNotExist:

                                        one=Logeado.objects.get(numId=3)
                                        one_entry = Paciente.objects.get(paciente_dni=one.usuarioLogeado)
                                        if  int(request.GET["pass"]) == one_entry.codigo :
                                            print('')

                                            today = date.today()

                                            age = today.year - one_entry.paciente_fechaNac.year - ((today.month, today.day) < (one_entry.paciente_fechaNac.month, one_entry.paciente_fechaNac.day))
                                            if (age >= 60):
                                                return render(request, "main/inicioPaciente.html",{"valor":3,"p":one_entry})
                                            else:

                                                try:
                                                    pasa= SolicitudTurnoFA.objects.get(dni=one_entry.paciente_dni)
                                                    return render(request, "main/inicioPaciente.html",{"valor":1,"p":one_entry})
                                                except ObjectDoesNotExist:
                                                    return render(request, "main/inicioPaciente.html",{"valor":2,"p":one_entry})


#############################################################
    # one = Logeado.objects.get(numId=3)
    #
    #
    # one_entry = Paciente.objects.get(paciente_dni=one.usuarioLogeado)

            # dni=models.IntegerField()
            # numId=models.IntegerField()
            # email= models.EmailField(max_length=254

                                            # except ObjectDoesNotExist:
                                            #     return render(request, "main/inicioPaciente.html",{"valor":2})
                                        #mensaje= request.GET["pass"]

                                                #return render(request,"main/inicioPaciente.html")
###################################################################
                                        else:

                                            messages.error(request, "codigo invalido")
                                            return render (request,"main/verif.html")



                                # if  int(request.GET["pass"]) == one_entry.codigo :
                                #     #mensaje= request.GET["pass"]
                                #
                                #     return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
                                # else:
                                #     messages.error(request, "codigo invalido")
                                #     return render (request,"main/verif.html")

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


# def reg_vac(request):
#
#     #data = {
#     #    "form": vacunador_signUpForm()}
#     #if request.method == "POST":
#      #    formulario = UserCreationForm(request.POST)
#       #   if formulario.is_valid():
#      #       user = formulario.save()
#
#      #       dni = form.cleaned_data["dni"]
#      #       user = authenticate(dni=dni)
#      #       login(request, user)
#      #       return redirect(to="login")
#
#     form= vacunador_signUpForm(request.POST or None)
#
#     if form.is_valid():
#         instance = form.save()
#         if Vacunador.objects.filter(dni= instance.vacunador_dni).exists():
#             messages.Warning(request, "El DNI ya existe")
#         else:
#             instance.save()
#             messages.success(request, "Enviamos un correro electronico a " + instance.vacunador_email)
#             #correo electronico
#
#             subject="Registro de Vacunador"
#             from_email= settings.EMAIL_HOST_USER
#             to_email=[instance.vacunador_email]
#
#             html_template="email_templates/welcome.html"
#             html_message=render_to_string(html_template)
#             message=EmailMessage(subject, html_message, from_email, to_email)
#             message.content_subtype="html"
#             message.send()
#     context={
#         'form': form,
#     }
#     return render(request, "main/registro_vacunador.html", context)

def send_email_registro(mail, codigo, dni, nombre):
    context = {"mail" : mail,
               "codigo" : codigo,
               "dni" : dni,
               "nombre" : nombre,
               }
    template = get_template("main/correo-registro.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Registro en VacunAssist ",
        "",
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
            digitos = '1234567890'
            longitud = 4  # La longitud que queremos
            codigo = ''.join(choice(digitos) for digito in range(longitud))
            send_email_registro(mail, codigo)
            context={
                'form': form,
                'codigo' : codigo,
            }
            return render(request, "main/registro_vacunador.html", context)
    context={
            'form': form,
        }
    return render(request, "main/registro_vacunador.html", context)

    if form.is_valid():
        form.save()

        return render(request,"main/inicio.html")
        #instance = form.save(commit=False)
        # if User.objects.filter(dni= instance.vacunador_dni).exists():
        #     messages.Warning(request, "El DNI ya existe")
        # else:
        #     instance.save()
        #     messages.success(request, "Enviamos un correro electronico a " + instance.vacunador_email)
        #     #correo electronico
        #
        #     subject="Registro de Vacunador"
        #     from_email= settings.EMAIL_HOST_USER
        #     to_email=[instance.vacunador_email]
        #
        #     html_template="email_templates/welcome.html"
        #     html_message=render_to_string(html_template)
        #     message=EmailMessage(subject, html_message, from_email, to_email)
        #     message.content_subtype="html"
        #     message.send()

    return render(request, "main/inicio_admin.html",context)
    # class reg_vac(View):
    #
    # def get(self, request):
    #    form = UserCreationForm()
    #    return render(request, "main/inicio_admin.html", {"form": form})
    #
    # def post(self, request):
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        user = form.save()
    #        dni_user = form.cleaned_data.get("dni")
    #        messages.success(request, F"Se ha registrado con exito {dni_user}")
    #        login(request, user)
    #        return redirect("main/login")
    #    else:
    #        for msg in form.error_messages:
    #            messages.error(request, form.error_messages[msg])

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

    return redirect("main/login")

    return redirect('main/login/')

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from secrets import choice

def send_email_pass(mail, contraseña, nombre):
    context = {"mail" : mail,
               "pass" : contraseña,
               "nombre" : nombre
               }
    template = get_template("main/correo-reset-pass.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Recuperar contraseña ",
        "probando envio de mails en django",
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, "text/html")
    email.send()



def reset_pass(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        mail = request.POST.get("mail")
        caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        longitud = 9  # La longitud que queremos
        contraseña = ''.join(choice(caracteres) for caracter in range(longitud))

        send_email_pass(mail, contraseña, dni)

    return render(request, "main/recuperar-contraseña.html", {})

def send_email_codigo(mail, contraseña, nombre):
    context = {"mail" : mail,
               "pass" : contraseña,
               "nombre" : nombre
               }
    template = get_template("main/correo-reset-codigo.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Recuperar código ",
        "",
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, "text/html")
    email.send()


def reset_codigo(request):
    if request.method == "POST":
        dni = request.POST.get("dni")
        mail = request.POST.get("mail")

        if request.POST.get("dni").isdigit():

        #mail= request.GET["dni"]
            try:
                usuario= Administrador.objects.get(administrador_dni = request.POST.get("dni"))
                email= usuario.administrador_email
                if (mail != email):
                    messages.error(request, "el mail ingresado no pertenece a un usuario Administrador")
                    return render(request, "main/recuperar-codigo.html")


            except ObjectDoesNotExist:
                try:
                    usuario= Vacunador.objects.get(vacunador_dni = request.POST.get("dni"))
                    email= usuario.vacunador_email
                    if (mail != email):
                        messages.error(request, "el mail ingresado no pertenece a un usuario Vacunador")
                        return render(request, "main/recuperar-codigo.html")

                except ObjectDoesNotExist:
                    try:
                        usuario= Paciente.objects.get(paciente_dni = request.POST.get("dni"))
                        email= usuario.paciente_email
                        if (mail != email):
                            messages.error(request, "el mail ingresado no pertenece a un usuario Paciente")
                            return render(request, "main/recuperar-codigo.html")

                    except ObjectDoesNotExist:
                        messages.error(request, "el dni ingresado no se esta asociado a un usuario del sistema")
                        return render(request, "main/recuperar-codigo.html", {})


        else:

            messages.error(request, "el dni debe ser un numero")
            return render(request, "main/recuperar-codigo.html")



    ### si todo sigue un flujo normal, se genera el nuevo codigo y se cambia el codigo en la base de datos
        #caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        digitos = '123456789'
        longitud = 4  # La longitud que queremos
        codigo = ''.join(choice(digitos) for digito in range(longitud))
        codigo = int(codigo)
        usuario.codigo=codigo


        usuario.save()
        #longitud = 4  # La longitud que queremos
        #contraseña = ''.join(choice(caracteres) for caracter in range(longitud))



        #send_email_codigo(mail, contraseña, dni)
        ## revisar


    return render(request, "main/recuperar-codigo.html", {"codigoq":codigo})



def index(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        longitud = 6  # La longitud que queremos
        contraseña = ''.join(choice(caracteres) for caracter in range(longitud))

        send_email_pass(mail, contraseña, "hola")

    return render(request, "main/index.html", {})



def reset_pass(request):
    if request.method == "POST":

        mail = request.POST.get("mail")
        if request.POST.get("dni").isdigit():

        #mail= request.GET["dni"]
        ################## voy buscando por tipo de usuario, hasta encontrar al dueño del dni
            try:
                usuario= Administrador.objects.get(administrador_dni = request.POST.get("dni"))
                email= usuario.administrador_email
                ## si los mails no coinciden , se recarga la pagina y se informa la razon
                if (mail != email):
                    messages.error(request, "el mail ingresado no pertenece a un usuario Administrador")
                    return render(request, "main/recuperar-contraseña.html")


            except ObjectDoesNotExist:
                try:
                    usuario= Vacunador.objects.get(vacunador_dni = request.POST.get("dni"))
                    email= usuario.vacunador_email
                    if (mail != email):
                        messages.error(request, "el mail ingresado no pertenece a un usuario Vacunador")
                        return render(request, "main/recuperar-contraseña.html")

                except ObjectDoesNotExist:
                    try:
                        usuario= Paciente.objects.get(paciente_dni = request.POST.get("dni"))
                        email= usuario.paciente_email
                        if (mail != email):
                            messages.error(request, "el mail ingresado no pertenece a un usuario Paciente")
                            return render(request, "main/recuperar-contraseña.html")

                    except ObjectDoesNotExist:
                        messages.error(request, "el dni ingresado no se esta asociado a un usuario del sistema")
                        return render(request, "main/recuperar-contraseña.html", {})


        else:

            messages.error(request, "el dni debe ser un numero")
            return render(request, "main/recuperar-contraseña.html")


###################################################        #######################

        # one_entry=Logeado.objects.all()[:1].get()

        ### si todo sigue un flujo normal, se genera la nueva contraseña y se cambia la contraseña en la base de datos

        caracteres = 'abcdefghijklmnopqrtsuvwxyz1234567890'
        longitud = 9  # La longitud que queremos
        contraseña = ''.join(choice(caracteres) for caracter in range(longitud))
        #contraseña= 334
        usuario.contraseña=contraseña
        usuario.save()

        # actualizo la contraseña

        #send_email(mail, contraseña)
        # revisar

    return render(request, "main/recuperar-contraseña.html", {})
