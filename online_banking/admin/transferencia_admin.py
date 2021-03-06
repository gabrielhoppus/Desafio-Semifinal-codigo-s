from django.contrib import admin
from online_banking.models.transferencia import Transferencia

"""Modelo que gera TransferĂȘncia dentro do Admin do Django"""
"""Lista os campos desejados e possibilita o registro de transferĂȘncias entre contas. """


class TransferenciaAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_id",
        "data_transferencia",
        "valor",
        "conta_origem",
        "conta_destino",
    )

    class Meta:
        verbose_name_plural = "TransferĂȘncias"


admin.site.register(Transferencia, TransferenciaAdmin)
