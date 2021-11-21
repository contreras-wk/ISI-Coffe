from django.urls import path
from rest_framework import routers

from .views import userAdd

from .viewsets import UsuarioViewSet

router = routers.SimpleRouter()
router.register('', UsuarioViewSet)

urlpatterns = [
    path('add/', userAdd),
] + router.urls