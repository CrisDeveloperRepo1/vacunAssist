from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView,PasswordResetDoneView
from django.urls import path, re_path, include, reverse_lazy
from .views import eliminar_Admin ,editarStockVacunatorio,cancelarTurno,eliminarSolicitud,empezarAsignacionTurno,AsignarTurno


app_name= 'main'

urlpatterns = [
    #path('', views.login1,name= 'homepage'),
    path('', views.main,name= 'main'),
    path('main/', views.main,name= 'main'),

    path('cancelarTurno/', views.cancelarTurno,name= 'cancelarTurno'),
    #path('compararCodigoPaciente/', views.compararCodigoPaciente,name= 'compararCodigoPaciente'),
    path('solicitarTurnoFA/', views.solicitarTurnoFA,name= 'solicitarTurnoFA'),
    path('inicioPaciente/', views.inicioPaciente,name= 'inicioPaciente'),
    path('loginPaciente/', views.loginPaciente , name="loginPaciente"),
    path('evaluarTurno/', views.evaluarTurno , name="evaluarTurno"),

    path('loginVacunador/', views.loginVacunador , name="loginVacunador"),
    path('loginAdmin/', views.loginAdmin , name="loginAdmin"),
    path('login/registro/', views.registro , name="registro"),
    path('login/', views.main, name= 'main' ),
    path('registrarPaciente/', views.registrarPaciente, name= 'registrarPaciente' ),
    path('registroPaciente/', views.registroPaciente, name= 'registroPaciente' ),

    path('AsignarTurno/', views.AsignarTurno, name= 'AsignarTurno' ),

    #path('register/', views.editarStockTotal, name= 'editarStockTotal' ),
    path('editarStockVacunatorio/', views.editarStockVacunatorio, name= 'editarStockVacunatorio' ),

    path('empezarAsignacionTurno/<int:dni>', views.empezarAsignacionTurno, name= 'empezarAsignacionTurno' ),
    path('eliminarVacunador/', views.eliminarVacunador, name= 'eliminarVacunador' ),
    path('eliminarSolicitud/<int:dni>', views.eliminarSolicitud , name="eliminarSolicitud"),


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
    path('registro_vacunador/' , views.reg_vac, name= "nuevo_vac"),
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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view()),

]
