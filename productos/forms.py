from django import forms
from django import productos


# aqui se crea el formulario de Productos
class FormularioProducto(forms.Form):
    Nombre = forms.CharField(max_length=200, label="Nombre del Producto")
    Marca = forms.CharField(max_length=200, label="Marca")
    Presentacion = forms.CharField(max_length=200, label="Presentacion")
    Descripcion = forms.CharField(max_length=200, label="Descripción")
    Precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio de Producto")
    Disponible = forms.BooleanField(initial=True, label="Disponible", required=False)
    Foto = forms.ImageField(label="Foto Producto", required=False)

    # crear datos dentro de la base de datos
    # clean_data: Un diccionario que contiene todos los datos del formulario después de haber sido validados y limpiados.
    def save(self):
        data = self.cleaned_data
        productos.objects.create(
            Nombre=data["Nombre del Producto"],
            Marca=data["Marca"],
            Presentacion=data["Presentacion"],
            Descripcion=data["Descripción"],
            Precio=data["Precio de Producto"],
            Disponible=data["Disponible"],
            Foto=data["Foto Producto"],
        )
