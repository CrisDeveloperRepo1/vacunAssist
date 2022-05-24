from django.db import models

# Create your models here.

class Vacunador(models.Model):
    vacunador_nombre= models.CharField(max_length=200)
    vacunador_apellido= models.CharField(max_length=20)
    vacunador_fechaNac= models.DateTimeField("fecha nacimiento")
    vacunador_zona= models.CharField(max_length=200)
    vacunador_dni= models.IntegerField()
    vacunador_email= models.EmailField(max_length=254)

    def __str__(self):
        return self

class Paciente(models.Model):
    opciones=((1, 'Si'), (2, 'No'))
    paciente_nombre= models.CharField(max_length=200)
    paciente_apellido= models.CharField(max_length=20)
    paciente_fechaNac= models.DateTimeField("fecha nacimiento")
    paciente_zona= models.CharField(max_length=200)
    paciente_dni= models.IntegerField()
    paciente_email= models.EmailField(max_length=254)
    vac_Gripe_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Gripe_turno= models.DateTimeField("turno_gripe")
    vac_Amarilla_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Amarilla_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Amarilla_turno= models.DateTimeField("turno_fa")
    vac_Amarilla_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid1_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid2_aplicada=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid_turno1= models.DateTimeField("turno_1era")
    vac_Covid_turno2= models.DateTimeField("turno_2da")
    vac_Covid1era_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    vac_Covid2da_asistencia=models.SmallIntegerField(choices=opciones,default=2)
    def __str__(self):
        return self.paciente_nombre

class Administrador(models.Model):
    administrador_nombre= models.CharField(max_length=200)
    administrador_apellido= models.CharField(max_length=20)
    administrador_fechaNac= models.DateTimeField("fecha nacimiento")
    administrador_zona= models.CharField(max_length=200)
    administrador_dni= models.IntegerField()
    administrador_email= models.EmailField(max_length=254)
    
    def __str__(self):
        return self.administrador_nombre
    
class Vacuna_Gripe(models.Model):
    vac_gripe_nombre= models.CharField(max_length=100)
    stock_vac_gripe=models.IntegerField()
    
    def __str__(self):
        return self
    
class Vacuna_Fiebre_Am(models.Model):
    vac_fa_nombre= models.CharField(max_length=100)
    stock_vac_fa=models.IntegerField()
    
    def __str__(self):
        return self
    
class Vacuna_Covid(models.Model):
    vac_covid_nombre= models.CharField(max_length=100)
    stock_vac_covid_1era=models.IntegerField()
    stock_vac_covid_2da=models.IntegerField()
    def __str__(self):
        return self
    
class Vacunatorio(models.Model):
    administrador_nombre= models.CharField(max_length=100)
    stock_vac_fa=models.IntegerField()
    stock_vac_covid=models.IntegerField()
    stock_vac_gripe=models.IntegerField()
    
    def __str__(self):
        return self