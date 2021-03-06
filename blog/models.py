from django.db import models
from django.contrib import admin
# Create your models here.

class Bus(models.Model):
    modelo_bus = models.CharField(max_length=4)
    placa_bus = models.CharField(max_length=15)
    no_asiento_bus = models.CharField(max_length=4)
    imagen_bus = models.ImageField(upload_to='media/Fotos/')

    def __str__(self):
        return self.placa_bus

class Asiento(models.Model):
    no_asiento=models.CharField(max_length=4)
    estado_asiento=models.CharField(max_length=1)
    id_bus=models.ForeignKey(Bus)

class Programacion(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    id_bus=models.ForeignKey(Bus)

    def __str__(self):
        return str(self.hora)

class Destino(models.Model):
    lugar_destino=models.CharField(max_length=50)
    valor_destino=models.CharField(max_length=5)

    def __str__(self):
        return self.lugar_destino

class Cliente(models.Model):
    NIT_cliente=models.CharField(max_length=10)
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=50)
    edad_cliente=models.CharField(max_length=2)
    genero_cliente=models.CharField(max_length=1)
    telefono_cliente=models.CharField(max_length=8)
    destinos = models.ManyToManyField(Destino, through='Reserva')
    programaciones=models.ManyToManyField(Programacion,through='Reserva')

    def __str__(self):
        return self.nombre_cliente

class Reserva(models.Model):
    fecha_reserva=models.DateField('fecha Reserva')
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    programacion=models.ForeignKey(Programacion,on_delete=models.CASCADE)
    destino=models.ForeignKey(Destino,on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_reserva

class ReservaInLine(admin.TabularInline):
    model=Reserva
    extra=1

class ClienteAdmin(admin.ModelAdmin):
    inlines = (ReservaInLine,)

class ProgramacionAdmin(admin.ModelAdmin):
    inlines = (ReservaInLine,)

class DestinoAdmin(admin.ModelAdmin):
    inlines = (ReservaInLine,)
