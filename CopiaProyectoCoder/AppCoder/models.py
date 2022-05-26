from django.db import models

# Create your models here.
class Cursor(models.Model): 
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    Email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    Email = models.EmailField()
    Profesion = models.CharField(max_length=30)

class entrega(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()