from django.db import IntegrityError
from rest_framework import serializers
from online_banking.models import Cliente
from online_banking.validators.letter_validator import valida_letra
from online_banking.validators.number_validator import valida_numero


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    """Define parâmetros e validações para os campos de cliente"""

    telefone = serializers.CharField(min_length=13)
    cpf = serializers.CharField(min_length=11)

    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_nome(self, nome):
        if valida_letra(nome):
            raise serializers.ValidationError(
                {"Nome": "Nome deve conter somente letras."}
            )
        return nome

    def validate_cep(self, cep):
        if valida_numero(cep):
            raise serializers.ValidationError({"CEP": "CEP deve ser numérico."})
        return cep

    def validate_cpf(self, cpf):
        if valida_numero(cpf):
            raise serializers.ValidationError({"CPF": "CPF deve ser numérico."})
        return cpf
