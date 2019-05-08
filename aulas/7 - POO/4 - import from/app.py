
from banco_v4 import *

conta = Banco("Lucas", 3000)

valor = float(input('Valor para depositar: R$'))
conta.depositar(valor)

valor = float(input('Valor para sacar: R$'))
conta.sacar(valor)

