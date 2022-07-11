from email import message
from genericpath import exists

# from core.erp.forms import SaleForm
# from core.erp.mixins import ValidatePermissionRequiredMixin
from django.views.generic import CreateView, ListView , DeleteView, UpdateView, View
# from core.erp.models import Sale, Product, DetSale
from random import random
from certifi import contents
from django.views import View
import django
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib.style import context
from numpy import datetime_as_string
from matplotlib.style import context
from .models import Vacunador, Envio_de_correo, Administrador,Vacunatorio, Dni, Paciente_ST
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
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacunador, Envio_de_correo, Administrador,Vacunatorio,Vacuna_Fiebre_Am,Vacuna_Covid,Paciente,SolicitudTurnoFA,Logeado,TurnoFAAprobados,Dni
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
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.contrib.auth import login, logout, authenticate



import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth.forms import UserCreationForm
from.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# def inicio_admin(request#     # data2= gfffikuj
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

def cerrarSesion(request):
    logout(request)
    #return render(request,'main/main.html')
    return redirect('/login/')

def login_request(request):
    #if request.method =='POST':
    #form =AuthenticationForm(request, data=request.POST)

    # usuario=request.GET["dni"]
    # contraseña=request.GET["pass"]
    user= authenticate(username='cristian',password=7823)
    login(request, user)
    #return (request,'main/inicio_de_sesión.html')

    # user= authenticate(username='cristian',password=7823)
    # if user is not None:
    #     login(request, user)
    #     return (request,'main/register2.html')

    return render(request,'main/editarStockVacunatorio.html')



def loginRestringido(request):
    return render(request,'main/loginRestringido.html')

def register2(request):
    # u=user.objects.get(Username='cristian')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form.save()
        if form.is_valid():
            form.save()
            #### hago prueba ###
            admin=Administrador.objects.get(administrador_dni=12345678)
            ap=request.POST['apellido']
            #admin.administrador_apellido=form.cleaned_data['password1']
            admin.administrador_apellido=ap
            admin.save()
            ##################
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario{username} creado')
            #return redirect('/login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request,'main/register2.html',context)
class SaleInvoicePdfView(View):

    def get(self, request, *args, **kwargs):
        template = get_template("main/pdfPrueba.html")
        context = {'title': 'mi primer pdf'}
        html=template.render(context)
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="comprobanteVacuna.pdf"'
        pisa_status = pisa.CreatePDF(
              html, dest=response)
    # if error then show some funny view
        # if pisa_status.err:
        #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
def editarPerfilAdmin (request):
    ### solo vista ########
    usuario=Logeado.objects.get(numId=1)
    paciente=Administrador.objects.get(administrador_dni=usuario.usuarioLogeado)
    context = { 'apellido': paciente.administrador_apellido,
                'nombre': paciente.administrador_nombre,
                'contraseña': paciente.contraseña,
                'zona': paciente.administrador_zona,
                'email': paciente.administrador_email,
                    }


    return render(request,"main/editarPerfilAdmin.html", context)
def accionEditarPerfil (request):
    usuario=Administrador.objects.get(administrador_dni=12345678)
    n=request.POST['nombre']


    z=request.POST['zona']
    usuario.administrador_zona=z
    usuario.administrador_nombre=n
    usuario.save()
    context = { 'apellido': usuario.administrador_apellido,
                'nombre': usuario.administrador_nombre,
                'contraseña': usuario.contraseña,
                'zona': usuario.administrador_zona,
                'email': usuario.administrador_email,
                    }


    # usuario=Logeado.objects.get(numId=3)
    # apellido=request.POST['apellido']
    #
    #
    #
    #
    # paciente=Paciente.objects.get(paciente_dni=usuario.usuarioLogeado)
    # context = { 'apellido': paciente.paciente_apellido,
    #             'nombre': paciente.paciente_nombre,
    #             'contraseña': paciente.contraseña,
    #             'zona': paciente.paciente_zona,
    #             'email': paciente.paciente_email,
    #                 }


    return render(request,"main/editarPerfilAdmin.html", context)

# def editarPerfilAdmin (request):
#     ### solo vista ########
#     usuario=Logeado.objects.get(numId=3)
#     paciente=Paciente.objects.get(paciente_dni=usuario.usuarioLogeado)
#     context = { 'apellido': paciente.paciente_apellido,
#                 'nombre': paciente.paciente_nombre,
#                 'contraseña': paciente.contraseña,
#                 'zona': paciente.paciente_zona,
#                 'email': paciente.paciente_email,
#                     }
#
#
#     return render(request,"main/editarPerfilAdmin.html", context)
# def accionEditarPerfil (request):
#     usuario=Logeado.objects.get(numId=3)
#     apellido=request.POST['apellido']
#
#
#
#
#     paciente=Paciente.objects.get(paciente_dni=usuario.usuarioLogeado)
#     context = { 'apellido': paciente.paciente_apellido,
#                 'nombre': paciente.paciente_nombre,
#                 'contraseña': paciente.contraseña,
#                 'zona': paciente.paciente_zona,
#                 'email': paciente.paciente_email,
#                     }
#
#
#     return render(request,"main/editarPerfilAdmin.html", context)
@login_required(login_url='/login/')
def registrarVacunador (request):
    admin=Administrador.objects.get(administrador_dni=12345678)
    #nombre=request.POST['nombre']

    apellido=request.POST['apellido']
    # admin.administrador_apellido=request.POST['apellido']
    # admin.save()

    nombre=request.POST['nombre']
    fechaNac=request.POST['birthday']
    zona=request.POST['vacunatorio']
    dni=request.POST['dni']
    email=request.POST['email']
    Contraseña=request.POST['contraseña']
    digitos = '0123456789'
    longitud = 4  # La longitud que queremos
    Codigo = ''.join(choice(digitos) for digito in range(longitud))
    #codigo=request.POST['dni']

#### agregar metodo q devuelva el ultimo objeto de la tabla
    vacunador=Vacunador.objects.create(vacunador_nombre=nombre,vacunador_apellido=apellido,vacunador_fechaNac=fechaNac,vacunador_zona=zona,vacunador_dni=dni,vacunador_email=email,codigo=Codigo,contraseña=Contraseña)

    fecha = datetime.strptime(fechaNac, "%Y-%m-%d")
    #resultado = (datetime.now().date().year - (fecha).year)
    resultado = (datetime.now().date() + relativedelta(years=-2))
    #resultado -= ((datetime.now().month) < (fecha.month)) and ((datetime.now().day) < (fecha.day))
    #print(resultado)

    send_email_registro(email, Codigo, dni, nombre)
    context = {
        'fecha_max': str(datetime.now().date()),
        'fecha_min': str(resultado),
    }
    print("hola")
    return render(request,"main/registro_vacunador.html", context)



def cancelarTurno (request):
#### agregar metodo q devuelva el ultimo objeto de la tabla
    usuario = Logeado.objects.get(numId=3)
    TurnoFA= TurnoFAAprobados.objects.get(dni=usuario.usuarioLogeado)
    TurnoFA.delete()
    paciente= Paciente.objects.get(paciente_dni=usuario.usuarioLogeado)
    paciente.vac_Amarilla_turno= None
    paciente.save()
    return render(request,"main/inicioPaciente.html",{"valor":2,"p":paciente})
@login_required(login_url='/login/')
def evaluarTurno(request):
    ListSolicitud= SolicitudTurnoFA.objects.all()

    if (ListSolicitud.exists()):
        print('')

    else:
        messages.error(request, " no hay solicitudes de turno en el listado")

    #return render(request, "main/eliminarVacunador.html",{"administradores" : administradorList})

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

def send_mail_pre_registro (email, dni, nombre):
    context = {"mail" : email,
               "dni" : dni,
               "nombre" : nombre
               }
    template = get_template("main/correo-pre-registro.html")
    content = template.render(context)

    email = EmailMultiAlternatives (
        "Finalización de registro en VacunAssist ",
        "",
        settings.EMAIL_HOST_USER,
        [email]
    )

    email.attach_alternative(content, "text/html")
    email.send()


def fin_reg_paciente_st (request):

    return render (request, "main/registrarPaciente.html", context)


    return render (request, "main/registrarPaciente.html")


def validar_dni_st (request):
    if (request.method == "GET"):
        dni= request.GET.get("dni")
        if Paciente_ST.objects.filter(pacienteST_dni = dni).exists() :
            paciente = Paciente_ST.objects.get(pacienteST_dni = dni)
            context = {
                'nombre' : paciente.pacienteST_nombre,
                'apellido' : paciente.pacienteST_apellido,
                'dni' : paciente.pacienteST_dni,
                'mail' : paciente.pacienteST_email,
                'vac_covid1' : paciente.vac_Covid1_aplicada,
                'vac_covid2' : paciente.vac_Covid2_aplicada,
                'vac_amarilla' : paciente.vac_Amarilla_aplicada,
                'vac_gripe' : paciente.vac_Gripe_aplicada,
                'dir' : "/validarDniST/",
                'fecha_actual': str(datetime.now().date()),
            }
            return render (request, "main/registrarPaciente.html", context)
        else:
            if (dni != None):
                messages.error(request, "El Dni es incorrecto")
            return render(request, "main/validar-dni.html")


def reg_paciente_st (request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    #fecha=request.POST['fechaesperada']
    dni=request.POST['dni']
    email=request.POST['email']
    #zona=request.POST['vacunatorio']
    #opGripe=request.POST['opcVacunaGripe']
    #opFA=request.POST['opcVacunaFA']
    #opCoviP1=request.POST['opcVacunaCovidP1']
    #opCoviP2=request.POST['opcVacunaCovidP2']
    opcion=request.POST["opcVacunas"]

    #Contraseña=request.POST['Contraseña']

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
    opGripe = opFA = opCoviP1 = opCoviP2 = 2
    turnoGripe = turnoFiebre = turnoCovid1 = turnoCovid2 = None
    asistenciaGripe = asistenciaCovid1 = asistenciaCovid2 = asistenciaFiebre= 2
    if (opcion == "1"):
        opGripe= 1
        asistenciaGripe = 1
        turnoGripe= datetime.now()
    if (opcion == "2"):
        opFA=1
        asistenciaFiebre = 1
        turnoFiebre= datetime.now()
    if (opcion == "3"):
        opCoviP1=1
        asistenciaCovid1 = 1
        turnoCovid1= datetime.now()
    if (opcion == "4"):
        opCoviP2=1
        asistenciaCovid2 = 1
        turnoCovid2= datetime.now()

    Paciente_ST.objects.create(vac_Covid2_aplicada=opCoviP2,
                                        vac_Covid1_aplicada=opCoviP1,
                                        vac_Amarilla_aplicada=opFA,
                                        vac_Gripe_aplicada=opGripe,
                                        pacienteST_nombre=nombre,
                                        pacienteST_apellido=apellido,
                                        pacienteST_dni=dni,
                                        pacienteST_email=email,
                                        vac_Gripe_turno= turnoGripe,
                                        vac_Covid_turno1= turnoCovid1,
                                        vac_Covid_turno2= turnoCovid2,
                                        vac_Amarilla_turno= turnoFiebre,
                                        vac_Covid1era_asistencia= asistenciaCovid1,
                                        vac_Covid2da_asistencia= asistenciaCovid2,
                                        vac_Amarilla_asistencia= asistenciaFiebre,
                                        vac_Gripe_asistencia= asistenciaGripe
                                        )

    send_mail_pre_registro(email, dni, nombre)
    return render(request, "main/registro-paciente-sin-turno.html", {'opc': opcion})

def inicio_vacuandor (request):
    return render(request, "main/inicio-vacunador.html")

def registrarPaciente(request):
    return render(request, "main/registrarPaciente.html")
def registroPaciente(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    fecha=request.POST['fechaesperada']
    dni=request.POST['dni']
    email=request.POST['email']
    zona=request.POST['vacunatorio']
    opGripe=request.POST['opcVacunaGripe']
    opFA=request.POST['opcVacunaFA']
    opCoviP1=request.POST['opcVacunaCovidP1']
    opCoviP2=request.POST['opcVacunaCovidP2']
    Contraseña=request.POST['Contraseña']

    inicio = datetime(2022, 6, 30)
    final =  datetime(2022, 9, 28)

    # random_date = inicio + (final - inicio) * random.random()
    # vacFaTurno = random_date
    random_turnoCovid = inicio + (final - inicio) * random.random()
    random_gripe = inicio + (final - inicio) * random.random()
    random_turnoCovid2 = inicio + (final - inicio) * random.random()
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

    if Paciente_ST.objects.filter(pacienteST_dni = dni ).exists():
        asistenciaGripe = asistenciaFiebre = asistenciaCovid1 = asistenciaCovid2 = 2
        turno_fiebre= None
        paciente_st = Paciente_ST.objects.get(pacienteST_dni = dni )
        if (opGripe == "1"):
            opGripe= 1
            random_gripe= paciente_st.vac_Gripe_turno
            asistenciaGripe = paciente_st.vac_Gripe_asistencia
            #turnoGripe= datetime.now()
        if (opFA == "1"):
            opFA= 1
            turno_fiebre = paciente_st.vac_Amarilla_turno
            asistenciaFiebre = paciente_st.vac_Amarilla_asistencia
            #turnoFiebre= datetime.now()
        if (opCoviP1 == "1"):
            opCoviP1= 1
            random_turnoCovid = paciente_st.vac_Covid_turno1
            asistenciaCovid1 = paciente_st.vac_Covid1era_asistencia
            #turnoCovid1= datetime.now()
            if (opCoviP2 == "1"):
                opCoviP2= 1
                random_turnoCovid2 = paciente_st.vac_Covid_turno2
                asistenciaCovid2 = paciente_st.vac_Covid2da_asistencia
        else:
            random_turnoCovid2= None
                #turnoCovid2= datetime.now()
        paciente=Paciente.objects.create(
            vac_Gripe_turno=random_gripe, vac_Gripe_aplicada=opGripe, vac_Gripe_asistencia= asistenciaGripe,
            vac_Covid_turno1= random_turnoCovid, vac_Covid1_aplicada=opCoviP1, vac_Covid1era_asistencia= asistenciaCovid1,
            vac_Covid2_aplicada=opCoviP2, vac_Covid_turno2=random_turnoCovid2, vac_Covid2da_asistencia=asistenciaCovid2,
            vac_Amarilla_aplicada=opFA, vac_Amarilla_turno=turno_fiebre, vac_Amarilla_asistencia=asistenciaFiebre,
                                         codigo=codigo, contraseña=Contraseña,
                                         paciente_nombre=nombre, paciente_apellido=apellido,
                                         paciente_fechaNac=fecha, paciente_zona=zona,
                                         paciente_dni=dni, paciente_email=email,
                                         )
        paciente_st.delete()
    else:
        paciente=Paciente.objects.create(vac_Covid2_aplicada=opCoviP2,vac_Covid1_aplicada=opCoviP1,vac_Amarilla_aplicada=opFA,vac_Gripe_aplicada=opGripe,codigo=codigo,contraseña=Contraseña,paciente_nombre=nombre,paciente_apellido=apellido,paciente_fechaNac=fecha,paciente_zona=zona,paciente_dni=dni,paciente_email=email,vac_Gripe_turno=random_gripe,vac_Covid_turno1= random_turnoCovid)

    #messages.error(request, " El paciente ya exite")





    send_email_registro(email, codigo, dni, nombre)
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
    one_entry=Paciente.objects.get(paciente_dni=request.POST['dni'])
    #l=Logeado.objects.get(numId=3)
    #l.usuarioLogeado=DNI
    #print(DNI)
    #l.save()

    #one1 = SolicitudTurnoFA.objects.get(dni=one_entry.paciente_dni)
    Email=one_entry.paciente_email
    one_entry.vac_Amarilla_turno=fecha
    one_entry.save()
    ############ se guarda en turnos aprobados ######################
    Turno=TurnoFAAprobados.objects.create(dni=DNI,numId=0,email=Email)
    ##### se elimina  la solicitud de la tabla de solicitud de turnos #############
    solicitud=SolicitudTurnoFA.objects.get(dni=DNI)
    solicitud.delete()


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

    if (administradorList.exists()):
        print('')

    else:
        messages.error(request, " no hay vacunadores en el listado")

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
@login_required(login_url='/login/')
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
#@login_required(login_url='/loginRestringido/')
def loginAdmin(request):
    try:
        one_entry = Logeado.objects.get(numId=1)

    except ObjectDoesNotExist:
        UsuarioLogeado=0
        NumId=1
        usuario=Logeado.objects.create(usuarioLogeado=UsuarioLogeado,numId=NumId)

    return render(request, "main/inicio_de_sesión.html")
    #return redirect('/validarUsuario/')
    #return redirect("/validarUsuario/")
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
@login_required(login_url='/login/')
def editarStockVacunatorio(request):

    # administradorList= Vacunatorio.objects.all()
    # VacunaFiebreAm= Vacuna_Fiebre_Am.objects.all()
    # VacunaCovid=Vacuna_Covid.objects.all()
    #one_entry = Logeado.objects.get(numId=2)
    vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
    vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
    vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')
    # Cementerio Municipal
    # Municipalidad
    # Terminal de Omnibús


    return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})
def accionDeEdicionStock(request):
    destino=Vacunatorio.objects.get(vacunatorio_zona=request.POST['destino'])
    if(request.POST['vacuna'] == "stock_vac_fa" ):
        try:
            if (request.POST['disminuir'] == "disminuir"):
                if(int(request.POST['cantidad']) > destino.stock_vac_fa):
                    print('la cantidad ingresada es mayor')
                    messages.error(request, " la cantidad ingresada es mayor")

                    vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
                    vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
                    vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')
                    stock = destino.stock_vac_fa
                    print(stock)
                    return render(request, "main/editarStockVacunatorio.html",{ "vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})

                else:
                    destino.stock_vac_fa=destino.stock_vac_fa-int(request.POST['cantidad'])
                    destino.save()
                    # destino.stock_vac_fa=destino.stock_vac_fa+int(request.POST['cantidad'])
                    # destino.save()
                # stock_vac_fa=models.IntegerField()
                # stock_vac_covid=models.IntegerField()
                # stock_vac_gripe
        except KeyError:
            if (request.POST['aumentar'] == "aumentar"):
                destino.stock_vac_fa=destino.stock_vac_fa + int(request.POST['cantidad'])
                destino.save()
                vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
                vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
                vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')
                return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})


    elif (request.POST['vacuna'] =="stock_vac_covid"):
        try:
            if (request.POST['disminuir'] == "disminuir"):
                if(int(request.POST['cantidad']) > destino.stock_vac_fa):
                    print('la cantidad ingresada es mayor')
                    messages.error(request, " la cantidad ingresada es mayor")

                    vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
                    vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
                    vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')

                    return render(request, "main/editarStockVacunatorio.html",{"destino": destino, "vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})

                else:
                    destino.stock_vac_covid=destino.stock_vac_covid-int(request.POST['cantidad'])
                    destino.save()
        except KeyError:
            if (request.POST['aumentar'] == "aumentar"):
                destino.stock_vac_covid=destino.stock_vac_covid + int(request.POST['cantidad'])
                destino.save()
                vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
                vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
                vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')
                return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})


    else:
        try:
            if (request.POST['disminuir'] == "disminuir"):
                if(int(request.POST['cantidad']) > destino.stock_vac_gripe):
                    print('la cantidad ingresada es mayor')
                    messages.error(request, " la cantidad ingresada es mayor")

                    vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
                    vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
                    vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')
                    return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})

                else:
                    destino.stock_vac_gripe=destino.stock_vac_gripe - int(request.POST['cantidad'])
                    destino.save()
        except KeyError:
            destino.stock_vac_gripe=destino.stock_vac_gripe + int(request.POST['cantidad'])
            destino.save()
            vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
            vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
            vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')

            return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})

    vacunatorioCementerio=Vacunatorio.objects.get(vacunatorio_zona='Cementerio Municipal')
    vacunatorioMunicipalidad=Vacunatorio.objects.get(vacunatorio_zona='Municipalidad')
    vacunatorioTerminal=Vacunatorio.objects.get(vacunatorio_zona='Terminal de Omnibus')

    return render(request, "main/editarStockVacunatorio.html",{"vacunatorioC":vacunatorioCementerio,"vacunatorioMuni":vacunatorioMunicipalidad,"vacunatorioTerm":vacunatorioTerminal})



@login_required(login_url='/login/')
def eliminarVacunador(request):
    vacunadoresList= Vacunador.objects.all()
    print("0")
    try:
        if request.POST["filtro"] :
            print("entre al if de dni")
            try:
                if Vacunador.objects.filter( vacunador_dni =  request.POST["filtro"]).exists():
                    print("1")
                    por_dni = {Vacunador.objects.get(vacunador_dni = request.POST["filtro"])}
                    return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'por_dni': por_dni, 'valor': 1})
                else:
                    return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'por_dni': [], 'valor': 1})
            except ValueError:
                try:
                    if Vacunador.objects.filter( vacunador_zona =  request.POST["filtro"]).exists():
                        print("1")
                        por_vacunatorio= {Vacunador.objects.get(vacunador_zona = request.POST["filtro"])}
                        return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'por_vacunatorio': por_vacunatorio,  'valor': 2})
                    else:
                        return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'por_vacunatorio': [],  'valor': 2})
                except :
                    return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList,  'valor': 0})
    except :
        return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'valor': 0})
    return render(request,"main/eliminarVacunador.html",{"vacunadores" :vacunadoresList, 'valor': 0})

    #administradorList= Vacunador.objects.all()

#    if (administradorList.exists()):
#        print('')

#    else:
#        messages.error(request, " no hay vacunadores en el listado")

    #return render(request, "main/eliminarVacunador.html",{"administradores" : administradorList})

    #return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})


def verif(request):
    return render(request,"main/verif.html")
@login_required(login_url='/login/')
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

    PacienteList= Paciente.objects.all()


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
    return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList,"paciente":PacienteList})
    #return render(request,'main/registro_Admin.html')

    return render(request, "main/inicio_admin.html",{"administradores" : administradorList, "vacunadores" : vacunadorList,"paciente":PacienteList})


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

                    messages.error(request, "  No pertenece a un usuario del sistema")
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

                    messages.error(request, " DNI o contraseña incorrecta")
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
                    messages.error(request, "  No pertenece a un usuario del sistema")
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
                #redirect("/verif/")
                user= authenticate(username='cristian',password=7823)
                login(request, user)
                #return redirect("/inicio_admin/")

                return render(request,"main/verif.html")

            else:
                messages.error(request, " DNI o contraseña incorrecta")
                return render(request,"main/inicio_de_sesión.html")

        except ObjectDoesNotExist:
           print("Either the blog or entry doesn't exist.")
           messages.error(request, " El dni ingresado no pertenece a un usuario del sistema")
           return render(request,"main/inicio_de_sesión.html") # vuelvo a la pagina
 #   else:
  #      messages.error(request, "El dni ingresado debe contener nmeros")
   #     return render(request,"main/inicio_de_sesión.html")


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


@login_required(login_url='/login/')
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
                                        PacienteList= Paciente.objects.all()
                                        administradorList= Administrador.objects.all()

                                        vacunadorList= Vacunador.objects.all()
                                        user= authenticate(username='cristian',password=7823)
                                        login(request, user)
                                        return redirect("/inicio_admin/")
                                        #return render(request, "main/inicio_admin.html",{"administradores" : administradorList, "vacunadores" : vacunadorList,"paciente":PacienteList})

                                    #mensaje= request.GET["pass"]

                                        #return render(request,"main/inicio_admin.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
                                    else:

                                        messages.error(request, "codigo invalido")
                                        return render (request,"main/verif.html")


                                except ObjectDoesNotExist:
                                    try:

                                        one=Logeado.objects.get(numId=2)
                                        one_entry = Vacunador.objects.get(vacunador_dni=one.usuarioLogeado)
                                        if  int(request.GET["pass"]) == one_entry.codigo :

                                        #mensaje= request.GET["pass"]

                                            return render(request,"main/inicio-vacunador.html",{"administradores" : administradorList,"vacunadores" :vacunadoresList})
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

    form= VacunadorRegistro(request.POST or None)
    print(request.method)
    if form.is_valid():
        print("entró al if ")
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
@login_required(login_url='/login/')
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
    #logout(request)
    #messages.info(request, "Tu sesión se cerró correctamente")
    return (request, "main/main.html")

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
               "codigo" : contraseña,
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
    codigo=''
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



        send_email_codigo(mail, codigo, dni)
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
                dni = usuario.administrador_dni
                ## si los mails no coinciden , se recarga la pagina y se informa la razon
                if (mail != email):
                    messages.error(request, "el mail ingresado no pertenece a un usuario Administrador")
                    return render(request, "main/recuperar-contraseña.html")


            except ObjectDoesNotExist:
                try:
                    usuario= Vacunador.objects.get(vacunador_dni = request.POST.get("dni"))
                    email= usuario.vacunador_email
                    dni = usuario.vacunador_dni
                    if (mail != email):
                        messages.error(request, "el mail ingresado no pertenece a un usuario Vacunador")
                        return render(request, "main/recuperar-contraseña.html")

                except ObjectDoesNotExist:
                    try:
                        usuario= Paciente.objects.get(paciente_dni = request.POST.get("dni"))
                        email= usuario.paciente_email
                        dni = usuario.paciente_dni
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

        send_email_pass(email, contraseña, dni)
        # revisar

    return render(request, "main/recuperar-contraseña.html", {})



#def verficacionDni(request):
    #r=request.POST.get('dni')
    #request.POST.get("dni")
    #

    #ListSolicitud= Dni.objects.all()
    #admin=Administrador.objects.get(administrador_dni=request.GET["dni"])




    try:
        ### agregar un if para q vea el tipo si es num o int
        datosDni=Dni.objects.get(num_dni=request.GET["dni"])
        #messages.error(request, "")
        return render(request, "main/registrarPaciente.html")
    except ObjectDoesNotExist:
        messages.error(request, "el dni no es valido")
        return render(request, "main/validar-dni.html")


        # if (int(num_dni=request.GET["dni"])):
        #     return render(request, "main/registrarPaciente.html")
        # else:
        #
        #     messages.error(request, "el dni no es valido")
        #     return render(request, "main/validar-dni.html")




def validarDni(request):
    contexto = {
                'dir' : "/validarDni/"
            }
    if (request.method == "GET"):
        dni= request.GET.get("dni")
        try:
            one = Dni.objects.get(num_dni = dni)
            if one.num_dni == dni:
                if Logeado.objects.filter(numId = 1).exists():
                    #le tuve que asignar numid = 1 porque el logueado
                    # al momento de registrar un vacunador es un administrador
                    try:
                        vacun = Vacunador.objects.get(vacunador_dni = dni)
                        messages.error(request, "El Dni ya está registrado")
                        return render(request, "main/validar-dni.html", contexto)
                    except ObjectDoesNotExist:
                       # log = Dni.objects.get(num_dni = dni)
                        resultado = (datetime.now().date() + relativedelta(years=-18))
                        context = { 'dni': one.num_dni,
                            'nombre': one.nombre,
                            'apellido': one.apellido,
                            'fecha_actual': str(datetime.now().date()),
                            'fecha_min': str(resultado),
                        }
                        #print(str(resultado))
                        return render(request, "main/registro_vacunador.html", context)

                if Logeado.objects.filter(numId = 3).exists():
                    try:
                        paciente = Paciente.objects.get(paciente_dni = dni)
                        messages.error(request, "El Dni ya está registrado")
                        return render(request, "main/validar-dni.html", contexto)
                    except ObjectDoesNotExist:
                       log = Dni.objects.get(num_dni = dni)
                       resultado = (datetime.now().date() + relativedelta(years=-18))
                       context = { 'dni': one.num_dni,
                            'nombre': one.nombre,
                            'apellido': one.apellido,
                            'fecha_actual': str(datetime.now().date()),
                            'fecha_min': str(resultado),
                        }
                       #print(str(resultado))
                       #print(log.num_dni + log.nombre + log.apellido)
                       return render(request, "main/registrarPaciente.html", context)
                if Logeado.objects.filter(numId = 2).exists():
                    print("hola entre en el logueado 2")
                    if Paciente_ST.objects.filter(pacienteST_dni = dni).exists() :
                        print ("entré al if del paciente")
                        messages.error(request, "El Dni ya inició el pre registro")
                        return render(request, "main/validar-dni.html", contexto)
                    else:
                        if Paciente.objects.filter(paciente_dni = dni).exists() :
                            print ("entré al else del paciente")
                            messages.error(request, "El Dni ya está registrado")
                            return render(request, "main/validar-dni.html", contexto)

                    log = Dni.objects.get(num_dni = dni)
                    resultado = (datetime.now().date() + relativedelta(years=-18))
                    context = { 'dni': one.num_dni,
                        'nombre': one.nombre,
                        'apellido': one.apellido,
                        'fecha_actual': str(datetime.now().date()),
                        'fecha_min': str(resultado),
                    }
                    #print(str(resultado))
                    #print(log.num_dni + log.nombre + log.apellido)
                    return render(request, "main/registro-paciente-sin-turno.html", context)

        except ObjectDoesNotExist:
            if (dni != None):
                messages.error(request, "El Dni es inválido ")
            return render(request, "main/validar-dni.html", contexto)

@login_required(login_url='/login/')
def lista_pacientes(request):
    PacienteList= Paciente.objects.all()
    print("0")
    try:
        if request.POST["filtro"] :
            print(Paciente.objects.filter( paciente_dni =  request.POST["filtro"]).exists())
            print(Paciente.objects.filter( paciente_zona =  request.POST["filtro"]).exists())
            try:
                if Paciente.objects.filter( paciente_dni =  request.POST["filtro"]).exists():
                    print("1")
                    por_dni = {Paciente.objects.get(paciente_dni = request.POST["filtro"])}
                    if len(por_dni) != 0:
                        return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'por_dni': por_dni, 'valor': 1})
                    else:
                        return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'por_dni': [], 'valor': 1})
                else: 
                    raise
            except :
                try:
                    print(Paciente.objects.filter( paciente_zona =  request.POST["filtro"]).exists())
                    if Paciente.objects.filter( paciente_zona =  request.POST["filtro"]).exists():
                        print("2")
                        por_vacunatorio= Paciente.objects.filter(paciente_zona = request.POST['filtro'])
                        return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'por_vacunatorio': por_vacunatorio,  'valor': 2})
                    else:
                        return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'por_vacunatorio': [],  'valor': 2})
                except :
                    return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList,  'valor': 0})
    except :
        return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'valor': 0})
    return render(request,"main/listado-pacientes.html",{"pacientes" :PacienteList, 'valor': 0})
@login_required(login_url='/login/')

def lista_administradores(request):
    administradorList= Administrador.objects.all()
    return render(request,"main/listado-administradores.html",{"administradores" : administradorList})
@login_required(login_url='/login/')
def lista_vacunadores(request):
    vacunadoresList= Vacunador.objects.all()
    print("0")
    try:
        if request.POST["filtro"] :
            print("entre al if de dni")
            try:
                if Vacunador.objects.filter( vacunador_dni =  request.POST["filtro"]).exists():
                    print("1")
                    por_dni = {Vacunador.objects.get(vacunador_dni = request.POST["filtro"])}
                    return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'por_dni': por_dni, 'valor': 1})
                else:
                    return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'por_dni': [], 'valor': 1})
            except ValueError:
                try:
                    if Vacunador.objects.filter( vacunador_zona =  request.POST["filtro"]).exists():
                        print("1")
                        por_vacunatorio= {Vacunador.objects.get(vacunador_zona = request.POST["filtro"])}
                        return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'por_vacunatorio': por_vacunatorio,  'valor': 2})
                    else:
                        return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'por_vacunatorio': [],  'valor': 2})
                except :
                    return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList,  'valor': 0})
    except :
        return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'valor': 0})
    return render(request,"main/listado-vacunadores.html",{"vacunadores" :vacunadoresList, 'valor': 0})
