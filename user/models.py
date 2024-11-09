from django.db import models

class Usuario (models.Model):
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200)
    nombre_usuario = models.CharField(max_length=200)
    emial = models.EmailField()
    contraseña = models.CharField(widget=models.PasswordInput)

    def __str__(self):
        return self.primer_nombre 

