from rest_framework import filters, generics
from online_banking.models.transferencia import Transferencia
from online_banking.serializers.transferencia_conta_serializer import (
    ListaTransferenciaContaSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

"""Módulo que determina o que será visível, editável e filtravél 
    na API de Transferências feitas por uma conta específica"""


class TransferenciaContaViewset(generics.ListAPIView):
    """Lista as transferências de uma conta"""

    def get_queryset(self):
        queryset = Transferencia.objects.filter(conta=self.kwargs["pk"])
        return queryset

    class DateRangeFilter(django_filters.FilterSet):
        """Gera um filtro que recebe a data inicial, final, ou a data exatada de um período especificado"""

        data_inicio = django_filters.DateFilter(
            field_name="data_transferencia", lookup_expr="gte"
        )
        data_fim = django_filters.DateFilter(
            field_name="data_transferencia", lookup_expr="lte"
        )
        data_transferencia = django_filters.DateFilter(
            field_name="data_transferencia", lookup_expr="exact"
        )

    serializer_class = ListaTransferenciaContaSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ["transacao_id"]
    filterset_class = DateRangeFilter
    filterset_fields = ["data_transferencia"]
