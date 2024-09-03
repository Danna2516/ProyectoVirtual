from django.views import generic
from .forms import FormularioProducto  # importa de un archivo a otro

# Las vistas son las funciones o clases que manejan las solicitudes HTTP y devuelven las respuestas correspondientes.
# Create your views here.


class VistaProducto(generic.FormView):
    template_name = "productos/add_productos.html"
    form_class = FormularioProducto
