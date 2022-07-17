from rest_framework import viewsets, filters, permissions
from online_banking.models import Conta
from online_banking.serializers.conta_serializer import ContaSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""Módulo que determina o que será visível, editável e filtravél na API de Contas"""


class ContaViewSet(viewsets.ModelViewSet):
    """Lista as contas criadas"""

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = ["conta"]
    ordering_fields = ["conta"]
