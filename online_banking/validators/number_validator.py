import re

"""Função que valida se o que foi digitado no campo
    contém somente números por meio de um regex"""


def valida_numero(data):
    """Valida se um campo contém somente digítos numéricos"""
    return not re.match(r"^([\s\d]+)$", data)
