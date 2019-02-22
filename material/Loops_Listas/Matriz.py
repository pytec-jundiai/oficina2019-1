
# REFAZER DANDO ERRO #

'''

O que é um Matriz?
Em python não existe nenhum comando para matriz, usamos os comandos de um array. Array nada mais é
que uma variável que possibilita armazenar vários caracteres ou valores, no mesmo espaço de memória.
Por isso, iremos tratar uma matrix da mesma forma que um array, com uma única diferença: enquanto o array
é unidimensional, a matriz é bidimensional (equivalente a uma tabela) com linhas e colunas.

Comandos úteis para Array ou Matriz:

 - append() para adicionar um elemento ao array na última posição
 - pop() para remover pelo índice
 - remove() para remover pelo valor ou nome
 - clear() para limpar todos os dados do array

'''


# Criação de uma Matriz
datas = [[1915, 1945, 1960, 1991], [2001, 2009, 2012, 2016]] # Perceba que há duas partes na declaração, logo

# Criação de uma Array
idades = [12, 22, 53, 75, 23]

'''
   A primeira parte da matriz: [1915, 1945, 1960, 1991]; é equivalente a primeira linha da tabela.
   Segunda parte: [2001, 2009, 2012, 2016]; linha seguinte, e assim sucessivamente conforme a quantidade de partes.

'''

# Limpando todos os dados da matriz ou array
datas.clear()
idades.clear()


# Removendo linha da matriz
datas.pop([1][0]) # A remoção é sempre por linha.


# Removendo pelo valor (Somente para Array ou Lista)
idades.remove(12)

# Adicionando um valor a Matriz ou Array
datas.append(1364)
idades.append(14)

# Imprimindo uma Matriz
print('Array:')
for x in idades:
    print(x)


# Imprimindo um Array
print('Matriz:')
for i in datas:
    print(i)

