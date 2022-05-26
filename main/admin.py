from django.contrib import admin
from .models import Vacunador
from .models import Paciente
from .models import Vacuna_Gripe
from .models import Vacuna_Fiebre_Am
from .models import Vacuna_Covid
from .models import Vacunatorio
from .models import Administrador

<<<<<<< HEAD
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
=======
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
>>>>>>> 7f69a281382c6688634b9e455d6c439489f6e3a3


admin.site.register(Vacunador)
admin.site.register(Paciente)
admin.site.register(Vacuna_Gripe)
admin.site.register(Vacuna_Fiebre_Am)
admin.site.register(Vacunatorio)
admin.site.register(Administrador)
admin.site.register(Vacuna_Covid)

# Register your models here.
