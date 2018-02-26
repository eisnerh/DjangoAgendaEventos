from django.contrib import admin
from Agenda.models import *
# Register your models here.
admin.site.register(Material)
admin.site.register(Evento)
admin.site.register(ClasificacionEvento)
admin.site.register(Cliente)
admin.site.register(DetalleEvento)
admin.site.register(EventoCliente)
admin.site.register(EventoMaterial)

