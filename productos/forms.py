from django import forms
from .models import productos


# aqui se crea el formulario de Productos
class FormularioProducto(forms.Form):
    Nombre = forms.CharField(max_length=200, label="Nombre del Producto")
    Marca = forms.CharField(max_length=200, label="Marca")
    Presentacion = forms.CharField(max_length=200, label="Presentacion")
    Descripcion = forms.CharField(max_length=200, label="Descripción")
    Precio = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio de Producto"
    )
    Disponible = forms.BooleanField(initial=True, label="Disponible", required=False)
    Foto = forms.ImageField(label="Foto Producto", required=False)

    # crear datos dentro de la base de datos
    def save(self):
        data = self.cleaned_data
        productos.objects.create(
            Nombre=data["Nombre"],
            Marca=data["Marca"],
            Presentacion=data["Presentacion"],
            Descripcion=data["Descripcion"],
            precio=data["Precio"],
            Disponible=data["Disponible"],
            Foto=data.get("Foto"),
        )
