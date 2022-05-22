from django.db import models

# Create your models here.

class Vacunador(models.Model):
    vacunador_nombre= models.CharField(max_length=200)
    # vacunador_apellido= models.CharField(max_length=20)
    # vacunador_fechaNac= models.DateTimeField("fecha nacimiento")
    # vacunador_zona= models.CharField(max_length=200)
    # vacunador_dni= models.IntegerField()
    # vacunador_email= models.EmailField(max_length=254)

    def __str__(self):
        return self.vacunador_nombre

class Paciente(models.Model):
    paciente_nombre= models.CharField(max_length=200)
    paciente_apellido= models.CharField(max_length=20)
    paciente_fechaNac= models.DateTimeField("fecha nacimiento")
    paciente_zona= models.CharField(max_length=200)
    paciente_dni= models.IntegerField()
    paciente_email= models.EmailField(max_length=254)
    paciente_asistencia= models.CharField(max_length=2)
    def __str__(self):
        return self.paciente_nombre

class Administrador(models.Model):
    administrador_nombre= models.CharField(max_length=200)
    administrador_apellido= models.CharField(max_length=20)
    administrador_fechaNac= models.DateTimeField("fecha nacimiento")
    administrador_zona= models.CharField(max_length=200)
    administrador_dni= models.IntegerField()
    administrador_email= models.EmailField(max_length=254)
    administrador_asistencia= models.CharField(max_length=2)
    def __str__(self):
        return self.administrador_nombre