from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import GetTokenPairSerializer

class GetTokenPairView(TokenObtainPairView):
    serializer_class = GetTokenPairSerializer