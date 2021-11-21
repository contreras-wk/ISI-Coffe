from django.contrib import admin

from .models import (TipoProducto, TamanoProducto, TipoPago)

admin.site.register(TipoProducto)
admin.site.register(TamanoProducto)
admin.site.register(TipoPago)