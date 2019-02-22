"-*- iso:8859-1 -*-"
'''
Módulos nada mais são que um conjunto de funções. Lembrando que módulo pode ser exterior(importado) ou interior(funções). 
Porque por definição, módulo é reaproveitamento de código.

Este módulo pode receber valores strings, uma vez que para cada função a conversão para um tipo primitivo específico.
'''


def somar(valor1, valor2):

    valor1 = int(valor1)
    valor2 = int(valor2)

    res = valor1 + valor2

    return res


def subtrair(valor1, valor2):
    valor1 = int(valor1)
    valor2 = int(valor2)

    res = valor1 - valor2

    return res


def multiplicar(valor1, valor2):
    valor1 = int(valor1)
    valor2 = int(valor2)

    res = valor1 * valor2

    return res


def dividir(valor1, valor2):
    # Convertendo valor recebido para float
    valor1 = float(valor1)
    valor2 = float(valor2)

    res = valor1 / valor2

    return res
