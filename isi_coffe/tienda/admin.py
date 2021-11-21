from django.contrib import admin

from .models import (
    Carrito,
    Producto,
    CarritoProducto,
    Compra,
)


admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(CarritoProducto)
admin.site.register(Compra)
