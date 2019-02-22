
# REFAZER DANDO ERRO #

'''

O que � um Matriz?
Em python n�o existe nenhum comando para matriz, usamos os comandos de um array. Array nada mais �
que uma vari�vel que possibilita armazenar v�rios caracteres ou valores, no mesmo espa�o de mem�ria.
Por isso, iremos tratar uma matrix da mesma forma que um array, com uma �nica diferen�a: enquanto o array
� unidimensional, a matriz � bidimensional (equivalente a uma tabela) com linhas e colunas.

Comandos �teis para Array ou Matriz:

 - append() para adicionar um elemento ao array na �ltima posi��o
 - pop() para remover pelo �ndice
 - remove() para remover pelo valor ou nome
 - clear() para limpar todos os dados do array

'''


# Cria��o de uma Matriz
datas = [[1915, 1945, 1960, 1991], [2001, 2009, 2012, 2016]] # Perceba que h� duas partes na declara��o, logo

# Cria��o de uma Array
idades = [12, 22, 53, 75, 23]

'''
   A primeira parte da matriz: [1915, 1945, 1960, 1991]; � equivalente a primeira linha da tabela.
   Segunda parte: [2001, 2009, 2012, 2016]; linha seguinte, e assim sucessivamente conforme a quantidade de partes.

'''

# Limpando todos os dados da matriz ou array
datas.clear()
idades.clear()


# Removendo linha da matriz
datas.pop([1][0]) # A remo��o � sempre por linha.


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

