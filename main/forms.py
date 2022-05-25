from django import forms
from .models import Vacunador, Envio_de_correo, Administrador


class vacunador_signUpForm (forms.ModelForm):
    class Meta:
        model = Vacunador
        fields =['vacunador_apellido']
        fields =['vacunador_fechaNac']
        fields =['vacunador_zona']
        fields =['vacunador_dni']
        fields =['vacunador_email']
        
class Vacunador_creationForm (forms.ModelForm):
    class Meta:
        model = Envio_de_correo
        fields = ['name','subject','body','email']

