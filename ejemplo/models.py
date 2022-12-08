from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    numero_pasaporte = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.nacimiento}, {self.numero_pasaporte}, {self.id}"
