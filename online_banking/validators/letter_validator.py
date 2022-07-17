import re

"""Função que valida se o que foi digitado no campo
    contém somente letras por meio de um regex"""


def valida_letra(data):
    """Valida se um campo contém apenas letras"""
    return not re.match(r"[A-Za-z]", data)
