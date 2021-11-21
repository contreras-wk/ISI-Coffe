from django.urls import path, include

from .views import GetTokenPairView

urlpatterns = [
    path('token/', GetTokenPairView.as_view()),
    path('usuarios/', include('clientes.urls')),
]