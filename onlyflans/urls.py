
from django.contrib import admin
from django.urls import path
from web.views import indice, acerca, bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name="indice"),
    path('acerca/', acerca, name="acerca"),
    path('bienvenido/', bienvenido, name="bienvenido"),
]
