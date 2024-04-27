from django.db import models

# Create your models here.
class vehiculo(models.Model):
    COLOR=(
        ('1', 'ROJO'),
        ('2', 'AZUL'),
        ('3', 'VERDE'),
    )
    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=20)
    modelo=models.IntegerField()
    color_vehiculo=models.CharField('color', max_length=1, choices=COLOR)
