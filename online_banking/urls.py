from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from online_banking.views.conta_viewset import ContaViewSet
from online_banking.views.transferencia_viewset import TransferenciaViewSet
from online_banking.views.cliente_viewset import ClienteViewSet
from online_banking.views.transferencia_conta_viewset import (
    TransferenciaContaViewset,
)

"""Registra as rotas e os caminhos para a comunicação da API Rest"""

router = routers.DefaultRouter()
router.register(r"cliente", ClienteViewSet)
router.register(r"conta", ContaViewSet)
router.register(r"transferencia", TransferenciaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("conta/<int:pk>/transferencia/", TransferenciaContaViewset.as_view()),
    path("transferencia/<int:pk>/transferencia/", TransferenciaContaViewset.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
