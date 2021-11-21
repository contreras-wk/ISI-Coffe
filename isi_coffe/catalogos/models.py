from django.db import models
from django.db.models.fields import DateField, DateTimeField


class TamanoProducto(models.Model):
    descipcion = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models,DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.descipcion}'


class TipoProducto(models.Model):
    descipcion = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models,DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.descipcion}'


class TipoTarjeta(models.Model):
    descipcion = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models,DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.descipcion}'


class TipoPago(models.Model):
    descipcion = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models,DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.descipcion}'


