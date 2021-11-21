from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework. permissions import AllowAny
from rest_framework.response import Response

from .serializers import UsuarioSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def userAdd(request):
    data = request.data
    serializer = UsuarioSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)