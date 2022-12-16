from django.db import models

# Create your models here.
class Reserva(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField() 
    institucion = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=50)