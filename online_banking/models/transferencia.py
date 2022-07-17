from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from online_banking.models.conta import Conta

"""Model de transferências com todos os campos a serem gerados no banco de dados"""


class Transferencia(models.Model):
    transacao_id = models.AutoField(primary_key=True, unique=True)
    data_transferencia = models.DateField(auto_now_add=True, null=True)
    valor = models.DecimalField(max_digits=65, decimal_places=2, null=True)
    conta = models.ForeignKey(
        Conta, on_delete=models.CASCADE, related_name="origem", null=True
    )
    conta_destino = models.ForeignKey(
        Conta, on_delete=models.CASCADE, related_name="destino", null=True
    )

    class Meta:
        verbose_name_plural = "Transferências"

    def __str__(self) -> str:
        return str(self.transaction_id).zfill(8)


"""Decorador receiver que instância as informações e atualiza 
    os saldos das contas envolvidas na transação"""


@receiver(post_save, sender=Transferencia)
def update_saldo(sender, instance, **kwargs):
    instance.conta_destino.saldo += instance.valor
    instance.conta.saldo -= instance.valor
    instance.conta_destino.save()
    instance.conta.save()
