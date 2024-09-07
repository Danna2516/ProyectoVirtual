from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

import productos
from .forms import FormularioProducto  # importa de un archivo a otro
from django.shortcuts import render
from django.views.generic import ListView
from productos.models import productos

from django.views.generic import ListView
from .models import productos
# Las vistas son las funciones o clases que manejan las solicitudes HTTP y devuelven las respuestas correspondientes.
# Create your views here.


class ProductoFormView(generic.FormView):
    template_name = "productos/add_productos.html"
    form_class = FormularioProducto
    success_url = reverse_lazy("agregar_producto")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# estas vistas se enruta en las urls

class productoListView(generic.ListView):
    model = productos
    template_name = 'productos/list_productos.html'
    context_object_name = 'productos'

