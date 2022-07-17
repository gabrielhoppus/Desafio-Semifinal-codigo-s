from rest_framework import viewsets, permissions, filters
from online_banking.models.transferencia import Transferencia
from online_banking.serializers.transferencia_serializer import TransferenciaSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""Módulo que determina o que será visível, editável e filtravél na API de Transferências"""


class TransferenciaViewSet(viewsets.ModelViewSet):
    """Lista as transferências efetuadas"""

    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    search_fields = [
        "transacao_id",
        "data_transferencia",
        "valor",
        "conta__conta",
        "conta_destino__conta",
    ]
    ordering_fields = ["transacao_id"]
