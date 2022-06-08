from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
#{'id': 1, 'nombre': 'Julio Javier', 'apellido': 'Medina', 'descripcion': 'Soltero y con hijos.', 'edad': 52, 'fdn': '1968-09-16', 'parentesco': 'Padre'},

class ModeloFamilia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    edad = models.IntegerField(null=False)
    fdn = models.DateField(null=False)
    parentesco = models.CharField(max_length=20, null=False)