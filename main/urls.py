from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView,PasswordResetDoneView
from django.urls import path, re_path, include, reverse_lazy

app_name= 'main'

urlpatterns = [
    path('', views.login,name= 'homepage'),
    path('login/registro/', views.registro , name="registro"),
    path('login/', views.login, name= 'login' ),

    path('accounts/login/', views.login, name= 'login' ),
    # path('login/verificación/' , views.verificacion, name= "verificacion"),
    path('inicio_admin/' , views.inicio_admin, name= "inicio_admin"),

    path('compararCodigo/' , views.compararCodigo, name= "compararCodigo"),

    path('sumarTotales/' , views.sumarTotales, name= "sumarTotales"),


    path('verif/' , views.verif, name= "verif"),
    path('validarUsuario/' , views.validarUsuario, name= "validarUsuario"),


    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac"),
    path('listarModelos/' , views.listarModelos, name= "listarModelos"),


    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac"),
    path('inicio_admin/eliminar_vacun/' , views.eliminar_vacunador, name= "eliminar_vacunador"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view()),

]
