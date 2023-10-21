from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Invitado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pareja(models.Model):
    nombre_novio = models.CharField(max_length=40)
    nombre_novia = models.CharField(max_length=40)
    fecha_casamiento = models.DateField()
    foto = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_novio} y {self.nombre_novia}"

class Regalo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pareja = models.ForeignKey(Pareja, on_delete=models.CASCADE)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    pareja = models.ForeignKey(Pareja, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentario de {self.autor} en la boda de {self.pareja.nombre_novio} y {self.pareja.nombre_novia}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}" 
