from django.db import models

class Inmueble(models.Model):
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=150)
    description = models.charField(max_length=500)
    imagen = models.charField(max_length=900)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.direccion