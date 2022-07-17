from django.test import TestCase
from online_banking.models import Conta, Cliente

"""Módulo de testes de contas"""


class TestConta(TestCase):
    def setUp(self):
        # Dado

        cliente = Cliente.objects.create(
            nome="Luiz",
            endereco="Rua do Antúrio",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="21625100",
            telefone="+5521975490141",
            cpf="13324531713",
            data_nascimento="1990-01-27",
        )

        Conta.objects.create(
            saldo=0.00,
            tipo_conta="C",
            cliente=cliente,
        )

    def test_conta_create(self):
        """Recebe as informações dadas
        e checa se a conta foi criada"""

        # Quando
        conta = Conta.objects.count()
        # Então
        self.assertEqual(conta, 1)
