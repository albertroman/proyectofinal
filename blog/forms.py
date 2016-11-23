from django import forms
from .models import Bus,Asiento,Programacion,Destino,Cliente,Reserva
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ingresarAsiento(forms.ModelForm):
    class Meta:
        model = Asiento
        fields = ('no_asiento', 'estado_asiento','id_bus')

class ingresarBus(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('modelo_bus', 'placa_bus','no_asiento_bus','imagen_bus')

class ingresarProgramacion(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ('fecha', 'hora','id_bus')

class ingresarDestino(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ('lugar_destino','valor_destino')

class ingresarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('NIT_cliente','nombre_cliente','apellido_cliente','edad_cliente','genero_cliente','telefono_cliente')

class ingresarReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('fecha_reserva','cliente','programacion','destino')

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
