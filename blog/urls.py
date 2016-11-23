from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required

urlpatterns = [

        url(r'^Registro/$', views.RegistroUsuario, name='nuevo_user'),

        url(r'^accounts/login/$',  login),
        url(r'^accounts/logout/$', logout),

        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

        url(r'^$', login),
        url(r'^inicio/$',views.inicio),
        url(r'^Bus/$',views.BusInicio),
        url(r'^Cliente/$', views.ClienteInicio),
        url(r'^Programacion/$',views.ProgramacionInicio),
        url(r'^Destinos/$', views.DestinoInicio),
        url(r'^Reserva/$',views.ReservaInicio),

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
        url(r'^ListaBusEditar/$',views.ListaBusEditar,name='lista'),
        url(r'^ListaProgramacionEditar/$',views.ListaProgramacionEditar,name='lista'),
        url(r'^ListaDestinoEditar/$',views.ListaDestinoEditar,name='lista'),
        url(r'^ListaReservaEditar/$',views.ListaReservaEditar,name='lista'),

        url(r'^ListaBusEliminar/$',views.ListaBusEliminar,name='lista'),
        url(r'^ListaClienteEliminar/$',views.ListaClienteEliminar,name='lista'),
        url(r'^ListaDestinoEliminar/$',views.ListaDestinoEliminar,name='lista'),
        url(r'^ListaProgramacionEliminar/$',views.ListaProgramacionEliminar,name='lista'),
        url(r'^ListaReservaEliminar/$',views.ListaReservaEliminar,name='lista'),

        url(r'^EditarCliente/(?P<pk>[0-9]+)/editar/$', views.EditarCliente, name='EditarCliente'),
        url(r'^EditarBus/(?P<pk>[0-9]+)/editar/$', views.EditarBus, name='EditarBus'),
        url(r'^EditarProgramacion/(?P<pk>[0-9]+)/editar/$', views.EditarProgramacion, name='EditarProgramacion'),
        url(r'^EditarDestino/(?P<pk>[0-9]+)/editar/$', views.EditarDestino, name='EditarDestino'),
        url(r'^EditarReserva/(?P<pk>[0-9]+)/editar/$', views.EditarReserva, name='EditarReserva'),

        url(r'^EliminarBus/(?P<pk>[0-9]+)/eliminar/$', views.EliminarBus, name='EliminarBus'),
        url(r'^EliminarCliente/(?P<pk>[0-9]+)/eliminar/$', views.EliminarCliente, name='EliminarCliente'),
        url(r'^EliminarDestino/(?P<pk>[0-9]+)/eliminar/$', views.EliminarDestino, name='EliminarDestino'),
        url(r'^EliminarProgramacion/(?P<pk>[0-9]+)/eliminar/$', views.EliminarProgramacion, name='EliminarProgramacion'),
        url(r'^EliminarReserva/(?P<pk>[0-9]+)/eliminar/$', views.EliminarReserva, name='EliminarReserva'),

    ]
