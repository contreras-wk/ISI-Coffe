from django.db.models import fields
from rest_framework import serializers

from .models import (
    TamanoProducto,
    TipoProducto,
    TipoPago,
)

class TamanoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamanoProducto
        fields = '__all__'


class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'


class TipoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPago
        fields = '__all__'