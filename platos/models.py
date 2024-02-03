from django.db import models
from datetime import time

class SubCategoria (models.Model):
    name = models.CharField(max_length=80)
    categoria = models.CharField(max_length=80, default="Especial")
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Plato (models.Model):
    name = models.CharField(max_length=80)
    historia = models.TextField()
    precio = models.FloatField()
    tiempo_elaboracion = models.TimeField(default=time(0,30,0))
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="img/", null=True)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name