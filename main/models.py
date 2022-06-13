from pyexpat import model
from unicodedata import name
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class SolicitudTurnoFA(models.Model):

    dni=models.IntegerField()
    numId=models.IntegerField()
    email= models.EmailField(max_length=254)



    def __int__(self):
        return self.dni
class Logeado(models.Model):

    usuarioLogeado=models.IntegerField()
    numId=models.IntegerField()



    def __int__(self):
        return self.usuarioLogeado
class Vacunador(models.Model):

    vacunador_nombre= models.CharField(max_length=200)

    vacunador_apellido= models.CharField(max_length=20)
    vacunador_fechaNac= models.DateTimeField("fecha nacimiento")
    vacunador_zona= models.CharField(max_length=200)
    vacunador_dni= models.IntegerField()
    vacunador_email= models.EmailField(max_length=254)
    vacunador_codigo= models.IntegerField()
    contraseña = models.IntegerField()


    def __str__(self):
        return self.vacunador_apellido

class Paciente(models.Model):
    opciones=((1, 'Si'), (2, 'No'))
    paciente_nombre= models.CharField(max_length=20)
    paciente_apellido= models.CharField(max_length=20)
    paciente_fechaNac= models.DateTimeField("fecha nacimiento")
    paciente_zona= models.CharField(max_length=200)
    paciente_dni= models.CharField(max_length=200)
    paciente_email= models.EmailField(max_length=254)
    vac_Gripe_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Gripe_turno= models.DateTimeField(null=True)
    vac_Amarilla_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Amarilla_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Amarilla_turno= models.DateTimeField(null=True)
    vac_Amarilla_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid1_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid2_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid_turno1= models.DateTimeField(null=True)
    vac_Covid_turno2= models.DateTimeField(null=True)
    vac_Covid1era_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid2da_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    paciente_codigo= models.PositiveIntegerField(default=0)
    contraseña = models.IntegerField()

    def __str__(self):
        return self.paciente_nombre

class Administrador(models.Model):
    administrador_nombre= models.CharField(max_length=200)
    administrador_apellido= models.CharField(max_length=20)
    administrador_fechaNac= models.DateTimeField("fecha nacimiento")
    administrador_zona= models.CharField(max_length=200)
    administrador_dni= models.IntegerField()
    contraseña = models.IntegerField()
    administrador_email= models.EmailField(max_length=254)
    administrador_codigo= models.IntegerField()

    def __str__(self):
        return self.administrador_nombre

class Vacuna_Gripe(models.Model):
    vac_gripe_nombre= models.CharField(max_length=100)
    stock_vac_gripe=models.IntegerField()

    def __str__(self):
        return self.vac_gripe_nombre

class Vacunatorio(models.Model):
    administrador_nombre= models.CharField(max_length=100)
    vacunatorio_zona= models.CharField(max_length=100)
    stock_vac_fa=models.IntegerField()
    stock_vac_covid=models.IntegerField()
    stock_vac_gripe=models.IntegerField()

    def __str__(self):
        return self.administrador_nombre

class Vacuna_Fiebre_Am(models.Model):
    vac_fa_nombre= models.CharField(max_length=100)
    stock_vac_fa=models.IntegerField()

    def __str__(self):
        return self.vac_fa_nombre

class Vacuna_Covid(models.Model):
    vac_covid_nombre= models.CharField(max_length=100)
    stock_vac_covid_1era=models.IntegerField()
    stock_vac_covid_2da=models.IntegerField()
    def __str__(self):
        return self.vac_covid_nombre

class Envio_de_correo (models.Model):
    name= models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body= models.TextField(blank=True, null=True)
    email= models.ManyToManyField(Vacunador)

    def __str__(self):
        return self.name
