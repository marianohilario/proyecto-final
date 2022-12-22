"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (mostrar_familiares, mostrar_mascotas, mostrar_vehiculos,
                            BuscarFamiliar, AltaFamiliar, AltaMascota, AltaVehiculo, ActualizarFamiliar, 
                            ActualizarMascota, ActualizarVehiculo, BorrarFamiliar, BorrarMascota, BorrarVehiculo)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('familia/', mostrar_familiares),
    path('mascota/', mostrar_mascotas),
    path('vehiculo/', mostrar_vehiculos),
    path('familia/buscar', BuscarFamiliar.as_view()),
    path('familia/alta', AltaFamiliar.as_view()),
    path('mascota/alta', AltaMascota.as_view()),
    path('vehiculo/alta', AltaVehiculo.as_view()),
    path('familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('vehiculo/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mascota/borrar/<int:pk>', BorrarMascota.as_view()),
    path('vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
]
