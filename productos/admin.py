from django.contrib import admin  # type: ignore
from .models import productos


#ESTO APENAS SE CONFIGURO NO HE CREADO EL SUPERUSUARIO
# Register your models here.
class productoAdmin(admin.ModelAdmin): #hereda del modelo de la aplicación
     model= productos
     list_display = ['Nombre', 'Marca', 'precio']
     search_fields =['Nombre']

admin.site.register(productos, productoAdmin) #nos permitira hacer modificaciones en el admin luego de que se use