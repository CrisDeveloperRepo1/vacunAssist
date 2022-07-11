from django import forms
from .models import Vacunador, Envio_de_correo, Administrador
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

from .models import Vacunador, Paciente,Envio_de_correo, Administrador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserRegisterForm(UserCreationForm):
    ### username ser la contraseña1 , por que los nombres de usuario deben ser unicos, y como vamos a tener dni repetidos , prefiero usar la contraseña como 
    username = forms.CharField(label='DNI', min_length=5, max_length=150)
    email = forms.EmailField()
    #Username= forms.EmailField(label='Contraseña')
    #### password1 sera el dni ####
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput )
    password2= forms.CharField(label='Comfirma Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class PacienteRegistro(ModelForm):
    class Meta:
        model = Vacunador
        fields = '__all__'
class VacunadorRegistro(ModelForm):
    class Meta:
        model = Vacunador
        fields = '__all__'
class CustomUserForm(UserCreationForm):

    # email = forms.EmailField()
    # password1= forms.CharField(label= 'contraseña', widget=forms.PasswordInput)
    #first_name= models.CharField(max_length=20)
    # # password2= forms.CharField(label= 'confirmar Contraseña', widget=forms.PasswordInput)
    # usuario_administrador = models.BooleanField(default = True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        #fields = ['username','email','password1']

class vacunador_signUpForm (forms.ModelForm):
    class Meta:
        model = Vacunador
        fields = '__all__'

class Vacunador_creationForm (forms.ModelForm):
    class Meta:
        model = Envio_de_correo
        fields = ['name','subject','body','email']
