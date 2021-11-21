from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # imagen usuario

    def __str__(self):
        return f'{self.usuario.username}'


class Direcciones(models.Model):
    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    codigo_postal = models.PositiveSmallIntegerField()
    calle = models.CharField(max_length=255)
    numero_exterior = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.id}'


class Tarjetas(models.Model):

    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # numero_tarjeta
    # numero_seguridad
    # fecha_vencimiento
    # tipo_tarjeta

    def __str__(self):
        return f'{self.id}'
