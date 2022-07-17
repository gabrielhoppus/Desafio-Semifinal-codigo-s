from rest_framework import serializers
from online_banking.models.transferencia import Transferencia


class ListaTransferenciaContaSerializer(serializers.ModelSerializer):
    """Serialização e campos disponíveis para o registro de transferências de um usuário"""

    transacao_id = serializers.ReadOnlyField(source="transferencia.transacao")
    conta = serializers.ReadOnlyField(source="conta.nome")

    class Meta:
        model = Transferencia
        fields = [
            "conta",
            "transacao_id",
            "data_transferencia",
            "valor",
            "conta",
        ]
