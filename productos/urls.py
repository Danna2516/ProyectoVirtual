from django.urls import path
from . import VistaProducto

urlpatterns = [
    path("agregar/", VistaProducto.as_view(), nomnbre="agregar nombre"),
]
