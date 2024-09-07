from django.urls import path
from .views import ProductoFormView, productoListView

  

urlpatterns = [
    path('', productoListView.as_view(), name='lista_producto'),#para cuando necesite enlista o agregar un nuevo producto
    path("agregar/", ProductoFormView.as_view(), name="agregar_producto"),
] 