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
        url(r'^ListaBus/$',views.ListaBus,name='lista'),
        url(r'^ListaProgramacion/$',views.ListaProgramacion,name='lista'),
        url(r'^ListaDestino/$',views.ListaDestino,name='lista'),
        url(r'^ListaCliente/$',views.ListaCliente,name='lista'),
        url(r'^ListaReserva/$',views.ListaReserva,name='lista'),
        url(r'^ListaClienteEditar/$',views.ListaClienteEditar,name='lista'),
        url(r'^EditarCliente/(?P<pk>[0-9]+)/editar/$', views.EditarCliente, name='EditarCliente'),
    ]
