from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    edad = models.IntegerField(null=False)
    fdn = models.DateField(null=False)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(null=False)
    fdn = models.DateField(null=False)

class Curso(models.Model):
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()
