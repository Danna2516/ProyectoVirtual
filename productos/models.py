from django.db import models

# Create your models here.
class productos(models.Model):
    Nombre = models.TextField(max_length=200, verbose_name="Nombre del Producto")# ayuda a que los nombres de los campos sean más comprensibles en la interfaz de usuario
    Descripcion= models.TextField (max_length=300, verbose_name="Descripcion del Producto")
    precio= models.DecimalField (max_digits=10, decimal_places=2, verbose_name="Precio (COP)")
    Disponible = models.BooleanField(default=True, verbose_name="Disponibles")
    Foto = models.ImageField(
        upload_to='logos/',  # Carpeta donde se almacenarán las imágenes
        verbose_name="Foto Producto",
        blank=True,  # Permite que el campo sea opcional
        null=True)    # Permite que el campo sea nulo en la base de datos
    
    def _str_(self):# en una clase, estás especificando cómo se debe mostrar el objeto cuando se convierte en una cadena
        return self.Nombre #se usa para definir cómo se debe representar un objeto como una cadena de texto (string)