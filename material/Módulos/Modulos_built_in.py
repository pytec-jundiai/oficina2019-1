'''
Material de apoio: BIBLIOTECAS

    Modulo: É um arquivo .py com diversas funções

    Pacote: É um conjunto de módulos

    Bibliotecas: É um conjunto de pacotes
'''

#aqui estamos importando a biblioteca math atravez do comando 'import'
#a biblioteca math possui diversos modulos matematicos

import math

#Calculando a raiz quadrada de um numero

num = int(input('Digite um numero: '))#o usuario entra com um numero

raiz = math.sqrt(num) #estamos usando o modulo sqrt que é usado para calcular a raiz quadrada de um numero
                      #sqrt vem de square que ingles significa RAIZ
print(f'A raiz quadrada de {num} é :',raiz)

#-----------------------------------------------------------------------------------------------------------

#Arredondando um numero para cima ou para baixo

cima = math.ceil(raiz) #o modulo ceil arredonda os numeros para cima
print(f'A raiz arredondada para cima é {cima}')

baixo = math.floor(raiz) #o modulo floor arredonda os numeros para baixo
print(f'A raiz arredondada para baixo é {baixo}')


#Em vez de importarmos a biblioteca math inteira podemos importar apenas os modulos especificos

from math import trunc #aqui estamos importanto APENAS o modulo 'trunc' da biblioteca math

n1 = 5.425872
n2 = 8.228
#o modulo trunc pega apenas a primeira casa de um numero
print(f'Numero: {trunc(n1)}')
print(f'Numero: {trunc(n2)}')

#-----------------------------------------------------------------------------------------------------------------


#Usando a biblioteca Random
#A biblioteca random significa 'aleatorio', ou seja, você pode gerar numeros aleatorios entre outras operações


import random #estamos importando a biblioteca ramdom e todas as suas funcionalidades

aleatorio = random.random() #o método random da clase random gera um numero aleatorio entre 0 e 1
print(f'O numero gerado foi {aleatorio}')


#Gerando numeros entre 0 e 10

num = random.randint(0,10) #o modulo randint gera numeros aleatorios entre 0 e 10
print(f'O numero aleatorio gerado foi {num}')


#O modulo choice tem a função de escolher um elemento dentre outros elementos

from random import choice #estou importando apenas o modulo choice

lista = []
escolha = 0

for c in range(0,5):
    num = int(input('Digite um numero: '))
    lista.append(num)
    escolha = choice(lista)

print(f'O numero escolhido foi {escolha}')

'''No programa acima estou usando o laço de repetição for para que o usuario entre com 5 numeros
   logo apos isso os numeros esta sendo armazenados em uma lista atravez do metodo append, apos isso
   estou criando uma variavel 'escolha' que esta recebendo o modulo CHOICE, ou seja, ele está escolhendo
   um dos numeros que foram armazenados na lista, entao esse numero é exibido.
'''