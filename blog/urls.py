from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^IngresarBus/$', views.IngresarBus, name='ingresar'),
        url(r'^IngresarAsiento/$', views.IngresarAsiento, name='ingresar'),

    ]
