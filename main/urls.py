from django.urls import path, include
from . import views
app_name= 'main'

urlpatterns = [
    path('', views.homepage,name= 'homepage'),
    path('login/registro/', views.registro , name="registro"),
    path('login/', views.login, name= 'login' ),
    path('login/verificación/' , views.verificar, name= "validar"),
    path('inicio_admin/' , views.inicio_adm, name= "inicio_adm"),
<<<<<<< HEAD
    path('validarCodigo/' , views.validarCodigo, name= "validarCodigo"),


=======
    path('login/recuperar_Contraseña/' , views.recup_contra, name= "recuperar_Cont"),
    path('inicio_admin/nuevo_vac/' , views.reg_vac, name= "nuevo_vac")
>>>>>>> 2c4c22bb9e68980502195e8185b6290b7536ff54
]
