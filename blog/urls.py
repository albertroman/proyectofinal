from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^IngresarBus/$', views.IngresarBus, name='ingresar'),
        url(r'^IngresarAsiento/$', views.IngresarAsiento, name='ingresar'),
        url(r'^IngresarProgramacion/$', views.IngresarProgramacion, name='ingresar'),
        url(r'^IngresarDestino/$', views.IngresarDestino, name='ingresar'),
        url(r'^IngresarCliente/$', views.IngresarCliente, name='ingresar'),
        url(r'^IngresarReserva/$', views.IngresarReserva, name='ingresar'),
    ]
