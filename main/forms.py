from django import forms
from .models import Vacunador, Envio_de_correo, Administrador


class vacunador_signUpForm (forms.ModelForm):
    pass
        
class Vacunador_creationForm (forms.ModelForm):
    class Meta:
        model = Envio_de_correo
        fields = ['name','subject','body','email']

