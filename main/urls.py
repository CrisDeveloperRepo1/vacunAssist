from django.urls import path, include
from . import views
app_name= 'main'

urlpatterns = [
    path('', views.login,name= 'homepage'),
    path('login/registro/', views.registro , name="registro"),
    path('login/', views.login, name= 'login' ),
    # path('login/verificación/' , views.verificacion, name= "verificacion"),
    path('inicio_admin/' , views.inicio_admin, name= "inicio_admin"),

    path('compararCodigo/' , views.compararCodigo, name= "compararCodigo"),

<<<<<<< HEAD
    path('verif/' , views.verif, name= "verif"),
    path('validarUsuario/' , views.validarUsuario, name= "validarUsuario"),


    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac"),

=======
    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac"),
    path('inicio_admin/eliminar_vacun/' , views.eliminar_vacunador, name= "eliminar_vacunador")
>>>>>>> 366198f3055e673ab56e63442417eecf3b4e0e35
]
