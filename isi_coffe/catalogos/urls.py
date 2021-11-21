from django.urls import path
from django.urls.resolvers import URLPattern

from .views import (
    tamanoProductoAll,
    tipoProductoAll,
    tipoPagoAll,
)

urlpatterns = [
    path('tamanoproducto/all/', tamanoProductoAll),
    path('tipoproducto/all/', tipoProductoAll),
    path('tipopago/all/', tipoPagoAll),
]