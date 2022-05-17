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
