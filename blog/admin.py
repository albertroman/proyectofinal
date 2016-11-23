from django.contrib import admin
from .models import Bus,Asiento,Programacion,Destino,Cliente,Reserva,ClienteAdmin,ProgramacionAdmin,DestinoAdmin

# Register your models here.
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Programacion,ProgramacionAdmin)
admin.site.register(Destino,DestinoAdmin)
admin.site.register(Bus)
admin.site.register(Reserva)
admin.site.register(Asiento)
