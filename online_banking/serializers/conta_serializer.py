from logging import exception
from rest_framework import serializers
from online_banking.models.conta import Conta
from django.core.exceptions import ObjectDoesNotExist


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    """Define parâmetros e validações para os campos de conta"""

    class Meta:
        model = Conta
        fields = "__all__"
