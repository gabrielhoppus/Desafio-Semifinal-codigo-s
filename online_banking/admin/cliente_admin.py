from django.contrib import admin
from online_banking.models.cliente import Cliente

"""Modelo que gera o Cliente dentro do Admin do Django"""
"""Lista os campos desejados e possibilita o registro de clientes. """


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "nome", "cpf")

    class Meta:
        verbose_name_plural = "Clientes"


admin.site.register(Cliente, ClienteAdmin)
