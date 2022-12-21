from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    numero_pasaporte = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.nacimiento}, {self.numero_pasaporte}, {self.id}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    nacimiento = models.DateField()

    def __str__(self):
      return f"{self.nombre}, {self.nacimiento}, {self.raza}, {self.id}"

class Vehiculos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.id}"