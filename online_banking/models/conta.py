from django.db import models
from online_banking.choices import ACCOUNT_DESCRIPTION
from online_banking.models.cliente import Cliente

"""Model de contas com todos os campos a serem gerados no banco de dados"""


class Conta(models.Model):
    conta = models.AutoField(primary_key=True, unique=True)
    saldo = saldo = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    tipo_conta = models.CharField(max_length=1, choices=ACCOUNT_DESCRIPTION)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Contas"

    def __str__(self) -> str:
        return str(self.conta).zfill(8)
