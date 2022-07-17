from django.test import TestCase
from online_banking.models import Cliente

"""Módulo de teste do Cliente"""


class TestCliente(TestCase):
    def setUp(self):
        # Dado

        Cliente.objects.create(
            nome="Luiz",
            endereco="Rua do Antúrio",
            cidade="Rio de Janeiro",
            estado="RJ",
            cep="21625100",
            telefone="+5521975490141",
            cpf="13324531713",
            data_nascimento="1990-01-27",
        )

    def test_cliente_create(self):
        """Recebe as informações dadas e testa se o cliente foi criado"""
        # Quando
        cliente = Cliente.objects.count()
        # Então
        self.assertEqual(cliente, 1)

    def test_cliente_create_field(self):
        """Recebe as informações dadas e testa
        se informações condizem com o que foi criado"""
        # Quando
        cliente = Cliente.objects.get(cpf="13324531713")
        # Então
        self.assertEqual(cliente.nome, "Luiz")
