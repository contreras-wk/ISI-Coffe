from django.db.models import query
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer

from .models import (
    TamanoProducto,
    TipoProducto,
    TipoPago,
)

from .serializers import (
    TamanoProductoSerializer,
    TipoProductoSerializer,
    TipoPagoSerializer,
)

@api_view(['GET'])
@permission_classes([AllowAny])
def tamanoProductoAll(request):
    queryset = TamanoProducto.objects.all()
    serializer = TamanoProductoSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def tipoProductoAll(request):
    queryset = TipoProducto.objects.all()
    serializer = TipoProductoSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def tipoPagoAll(request):
    queryset = TipoPago.objects.all()
    serializer = TipoPagoSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)