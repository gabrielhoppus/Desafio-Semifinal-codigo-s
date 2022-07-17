from django.test import TestCase
from online_banking.models import Conta, Cliente, Transferencia

"""Módulo de testes das transferências"""


class TestTransferencia(TestCase):
    def setUp(self):
        # Dado

        cliente1 = Cliente.objects.create(
            nome="Luiz",
            endereco="Rua do Antúrio",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="21625100",
            telefone="+5521975490141",
            cpf="13324531713",
            data_nascimento="1990-01-27",
        )

        cliente2 = Cliente.objects.create(
            nome="Luiz Gabriel",
            endereco="Rua do Antúrio",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="21625100",
            telefone="+5521975490141",
            cpf="13324531714",
            data_nascimento="1990-01-27",
        )

        conta1 = Conta.objects.create(
            conta=1,
            saldo=250.00,
            tipo_conta="C",
            cliente=cliente1,
        )

        conta2 = Conta.objects.create(
            conta=2,
            saldo=240.00,
            tipo_conta="C",
            cliente=cliente2,
        )

        Transferencia.objects.create(
            transacao_id=1,
            valor=100.00,
            conta=conta1,
            conta_destino=conta2,
        )

    def test_transferencia_create(self):
        """Recebe as informações dadas
        e checa se a transferência ocorreu"""

        # Quando
        transferencia = Transferencia.objects.count()
        # Então
        self.assertEqual(transferencia, 1)

    def test_transferencia_valor(self):
        """Recebe as informações dadas
        e checa se a transferência ocorreu com o valor correto"""

        # Quando
        transferencia = Transferencia.objects.get(valor=100)
        # Então
        self.assertEqual(transferencia.valor, 100)

    def test_transferencia_saldo(self):
        """Recebe as informações dadas
        e checa se a transferência atualizou
        os saldos das contas envolvidas"""

        # Quando
        conta1 = Conta.objects.get(conta=1)
        conta2 = Conta.objects.get(conta=2)
        # Then
        self.assertEqual(conta1.saldo, 150)
        self.assertEqual(conta2.saldo, 340)
