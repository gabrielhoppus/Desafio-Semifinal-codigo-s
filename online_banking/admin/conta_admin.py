from django.contrib import admin
from online_banking.models.conta import Conta

"""Modelo que gera Conta dentro do Admin do Django"""
"""Possibilita o registro de contas. """


class ContaAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Contas"


admin.site.register(Conta, ContaAdmin)
