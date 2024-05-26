from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.titulo}'