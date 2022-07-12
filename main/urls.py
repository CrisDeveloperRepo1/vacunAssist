from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView,PasswordResetDoneView
from django.urls import path, re_path, include, reverse_lazy
from .views import eliminar_Admin ,editarStockVacunatorio,cancelarTurno,eliminarSolicitud,empezarAsignacionTurno,AsignarTurno,registrarVacunador,accionDeEdicionStock,Dni,editarPerfilAdmin,SaleInvoicePdfView,accionEditarPerfil,accionEditarPerfilPaciente,editarPerfilPaciente


app_name= 'main'

urlpatterns = [
    #path('', views.login1,name= 'homepage'),
    path('', views.main,name= 'main'),
    path('main/', views.main,name= 'main'),
    path('editarPerfilAdmin/', views.editarPerfilAdmin,name= 'editarPerfilAdmin'),
    path('register2/', views.register2,name= 'register2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cerrarSesion/', views.cerrarSesion, name = "cerrarSesion"),

    path('editarPerfilAdmin/', views.editarPerfilAdmin, name = "editarPerfilAdmin"),
    path('accionEditarPerfil/', views.accionEditarPerfil, name = "accionEditarPerfil"),
    path('accionEditarPerfilPaciente/', views.accionEditarPerfilPaciente, name = "accionEditarPerfilPaciente"),

    path('editarPerfilPaciente/', views.editarPerfilPaciente , name = "editarPerfilPaciente"),
    path('registrar_asistencia/', views.reg_asistencia , name = "registrarAsistencia"),
    path('asistencia/<int:id>/<int:res>/<str:vac>',views.asistencia),

    path('login_request/', views.login_request,name= 'login_request'),

    path('loginRestringido/', views.loginRestringido,name= 'loginRestringido'),

    path('accionEditarPerfil/', views.accionEditarPerfil,name= 'accionEditarPerfil'),
    path('SaleInvoicePdfView/', SaleInvoicePdfView.as_view(),name= 'sale_invoice_pdf'),
    # path('notificacion/', views.notificacion,name= 'notificacion'),

    path('cancelarTurno/', views.cancelarTurno,name= 'cancelarTurno'),
    #path('compararCodigoPaciente/', views.compararCodigoPaciente,name= 'compararCodigoPaciente'),
    path('solicitarTurnoFA/', views.solicitarTurnoFA,name= 'solicitarTurnoFA'),
    path('inicioPaciente/', views.inicioPaciente,name= 'inicioPaciente'),
    path('loginPaciente/', views.loginPaciente , name="loginPaciente"),
    path('evaluarTurno/', views.evaluarTurno , name="evaluarTurno"),
    path('inicioVacunador/', views.inicio_vacuandor, name= 'inicioVacunador'),
    path('registrarPacienteST/', views.reg_paciente_st , name="registrarVacunador"),
    path('finRegistroPacienteST/', views.fin_reg_paciente_st , name="registrarVacunador"),
    path('validarDniST/', views.validar_dni_st, name= 'validarDni' ),

    path('accionDeEdicionStock/', views.accionDeEdicionStock , name="accionDeEdicionStock"),
    path('registrarVacunador/', views.registrarVacunador , name="registrarVacunador"),

    path('loginVacunador/', views.loginVacunador , name="loginVacunador"),
    path('loginAdmin/', views.loginAdmin , name="loginAdmin"),
    path('login/registro/', views.registro , name="registro"),
    path('login/', views.main, name= 'main' ),
    path('registrarPaciente/', views.registrarPaciente, name= 'registrarPaciente' ),
    path('registroPaciente/', views.registroPaciente, name= 'registroPaciente' ),
    path('validarDni/', views.validarDni, name= 'validarDni' ),

    #path('verficacionDni/', views.verficacionDni, name= 'verficacionDni' ),

    path('AsignarTurno/', views.AsignarTurno, name= 'AsignarTurno' ),

    #path('register/', views.editarStockTotal, name= 'editarStockTotal' ),
    path('editarStockVacunatorio/', views.editarStockVacunatorio, name= 'editarStockVacunatorio' ),

    path('empezarAsignacionTurno/<int:dni>', views.empezarAsignacionTurno, name= 'empezarAsignacionTurno' ),
    path('eliminarVacunador/', views.eliminarVacunador, name= 'eliminarVacunador' ),
    path('eliminarSolicitud/<int:dni>', views.eliminarSolicitud , name="eliminarSolicitud"),
    path('lista-de-administradores/', views.lista_administradores, name= 'lista_administradores' ),
    path('lista-de-vacunadores/', views.lista_vacunadores, name= 'lista_vacunadores' ),
    path('lista-de-pacientes/', views.lista_pacientes, name= 'lista_pacientes' ),
    path('eliminar_Admin/<int:id>/<str:nombre>',views.eliminar_Admin),

    path('accounts/login/', views.login1, name= 'login' ),
    # path('login/verificación/' , views.verificacion, name= "verificacion"),
    path('inicio_admin/' , views.inicio_admin, name= "inicio_admin"),

    path('compararCodigo/' , views.compararCodigo, name= "compararCodigo"),

    path('sumarTotales/' , views.sumarTotales, name= "sumarTotales"),


    path('verif/' , views.verif, name= "verif"),
    path('validarUsuario/' , views.validarUsuario, name= "validarUsuario"),


    path('recuperar_codigo/' , views.reset_codigo, name= "recuperar_codigo"),
    path('recuperar_Contraseña/' , views.reset_pass, name= "recuperar_Cont"),
    path('registroVacunador/' , views.reg_vac, name= "nuevo_vac"),
    path('listarModelos/' , views.listarModelos, name= "listarModelos"),
    path('inicio_admin/actualizar/' , views.actualizar_stock, name= "listarModelos"),
#------------ url index solo para probar envio de mails ------------
    path('index/' , views.index, name= "index"),
    path('index/correo' , views.send_email_pass, name= "correo"),
#---------------------------------------------------------------------



    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac"),
    path('inicio_admin/eliminar_vacun/' , views.eliminar_vacunador, name= "eliminar_vacunador"),
    path('logout/', views.cerrar_sesion, name = "logout"),
    path('cerrar_sesion/', views.cerrar_sesion, name = "cerrar_sesion"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view()),

]
