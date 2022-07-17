from rest_framework import serializers
from online_banking.models import Transferencia


class TransferenciaSerializer(serializers.HyperlinkedModelSerializer):
    """Define parâmetros e validações para os campos de transferência"""

    class Meta:
        model = Transferencia
        fields = "__all__"
