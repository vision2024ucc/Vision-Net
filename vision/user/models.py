from django.db import models

class Usuario (models.Model):
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    email = models.EmailField(default='example@example.com')
    contraseña = models.CharField(max_length=200)

    def __str__(self):
        return self.primer_nombre 
    
from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='publicaciones/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    