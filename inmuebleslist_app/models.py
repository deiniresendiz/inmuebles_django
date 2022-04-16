from turtle import update

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Emperesa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.UrlField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Edificacion(models.Model):
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=150)
    description = models.charField(max_length=500)
    imagen = models.charField(max_length=900)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Emperesa, on_delete=models.CASCADE, related_name='edificaciones')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion


class Comentario(models.Model):
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True, blank=True)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name='comentarios')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.calificacion) * " " + self.edificacion.direccion