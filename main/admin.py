from django.contrib import admin
from .models import Vacunador
from .models import Paciente
from .models import Vacuna_Gripe
from .models import Vacuna_Fiebre_Am
from .models import Vacuna_Covid
from .models import Vacunatorio
from .models import Administrador

admin.site.register(Vacunador)
admin.site.register(Paciente)
admin.site.register(Vacuna_Gripe)
admin.site.register(Vacuna_Fiebre_Am)
admin.site.register(Vacunatorio)
admin.site.register(Administrador)
admin.site.register(Vacuna_Covid)

# Register your models here.
