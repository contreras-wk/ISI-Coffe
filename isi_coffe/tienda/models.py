from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField()
    tamano = models.ForeignKey('catalogos.TamanoProducto', on_delete=models.CASCADE)
    tipo_producto = models.ForeignKey('catalogos.TipoProducto', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'self.descripcion'


class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    # def __str__(self):
    #     return f'{}'
    pass


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    estatus = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actu = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    fecha_compra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'