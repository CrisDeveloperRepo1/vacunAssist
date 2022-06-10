from django.contrib import admin
from .models import Vacunador
from .models import Paciente
from .models import Vacuna_Gripe
from .models import Vacuna_Fiebre_Am
from .models import Vacuna_Covid
from .models import Vacunatorio, SolicitudTurnoFA
from .models import Administrador,Logeado


# class VacunadoresList(admin.ModelAdmin):
#     list_display= ["vacunador_nombre", "vacunador_apellido",
#                     "vacunador_zona", "vacunador_dni" ]
#     list_per_page: 5
#     list_filter= ["vacunador_dni", "vacunador_zona"]
#
# class AdministradoresList(admin.ModelAdmin):
#     list_display= ["administrador_nombre", "administrador_apellido",
#                     "administrador_dni" ]
#     list_per_page: 5
#     list_filter= ["administrador_dni"]

class VacunadoresList(admin.ModelAdmin):
    list_display= ["vacunador_nombre", "vacunador_apellido",
                    "vacunador_zona", "vacunador_dni" ]
    list_per_page: 5
    list_filter= ["vacunador_dni", "vacunador_zona"]

class AdministradoresList(admin.ModelAdmin):
    list_display= ["administrador_nombre", "administrador_apellido",
                    "administrador_dni" ]
    list_per_page: 5
    list_filter= ["administrador_dni"]



admin.site.register(Vacunador)
admin.site.register(Paciente)
admin.site.register(Vacuna_Gripe)
admin.site.register(Vacuna_Fiebre_Am)
admin.site.register(Vacunatorio)
admin.site.register(Administrador)
admin.site.register(Vacuna_Covid)
admin.site.register(Logeado)

admin.site.register(SolicitudTurnoFA)
# Register your models here.
