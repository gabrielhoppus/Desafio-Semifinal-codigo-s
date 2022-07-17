from rest_framework import viewsets, permissions, filters
from online_banking.models.cliente import Cliente
from online_banking.serializers.cliente_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""Módulo que determina o que será visível, editável e filtravél na API de Clientes"""


class ClienteViewSet(viewsets.ModelViewSet):
    """Lista os clientes cadastrados"""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = ["nome", "cpf", "endereco", "data_nascimento"]
    ordering_fields = ["nome"]
