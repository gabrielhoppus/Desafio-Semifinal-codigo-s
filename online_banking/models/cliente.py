from asyncio.windows_events import NULL
import uuid
from django.db import models
from online_banking.choices import STATE_CHOICES

"""Model do cliente com todos os campos a serem gerados no banco de dados"""


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=75, default="")
    endereco = models.CharField(max_length=100, default="")
    cidade = models.CharField(max_length=50, default="")
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)
    cep = models.CharField(max_length=8, default="")
    telefone = models.CharField(max_length=14, default="")
    cpf = models.CharField(max_length=11, unique=True, null=True)
    data_nascimento = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return str(self.id_cliente).zfill(8)
