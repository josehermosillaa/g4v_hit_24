
from django.contrib import admin
from django.urls import path, include
from web.views import indice, acerca, bienvenido,contacto, exito, MiVistaProtegida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name="indice"),
    path('acerca/', acerca, name="acerca"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    path('contacto/', contacto, name="contacto"),
    path('exito/', exito, name="exito"),
    path('prueba/', MiVistaProtegida.as_view(), name="prueba"),
    path('accounts/',include('django.contrib.auth.urls')),
]
