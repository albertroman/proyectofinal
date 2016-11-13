from django import forms
from .models import Bus,Asiento,Programacion,Destino,Cliente,Reserva


class ingresarAsiento(forms.ModelForm):
    class Meta:
        model = Asiento
        fields = ('no_asiento', 'estado_asiento','id_bus')

class ingresarBus(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('modelo_bus', 'placa_bus','no_asiento_bus')
