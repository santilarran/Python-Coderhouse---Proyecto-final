from pickletools import decimalnl_long, decimalnl_short
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User




class ObjetoVenta(models.Model):

    def __str__(self):

        return f"Objeto: {self.objeto} -------- fecha de subida: {self.fecha}"

    objeto = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=300)
    fecha = models.DateField()
    precio = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)

