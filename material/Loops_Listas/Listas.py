# Listas

lista = [0, 1, 2, 3]

# append() adiciona elementos no final lista
lista.append(5) 
print('append:', lista)

lista = [0, 1, 2, 3]

print('\n')

lista2 = [0, 0, 0, 0]

# extend() adiciona elementos de uma lista em outra lista
lista.extend(lista2)
print('extend:', lista)

lista = [0, 1, 2, 3]

# append() adiciona a lista inteira, não apenas seus elementos
lista.append(lista2)
print('append:', lista)

lista = [0, 1, 2, 3]
print('\n')

# insert() adiciona elementos em uma lista em uma posição especifica
# 2° posição aparecerá 800
lista.insert(1,800)
print(lista)

print('\n')

# Deletando elementos de uma lista
del lista[1]
print(lista)

print('\n')

# pop() apaga o último elemento da lista, mas também é possivel definir índice
lista = [0, 1, 2, 3]

lista.pop()
print('pop():', lista)

# remove() apaga o valor indicado

lista = [0, 1, 2, 3, 800]
print('antes do remove():', lista)
lista.remove(800)
print('depois remove():', lista)

print('\n')

# Mudando elementos de uma lista
lista = [0, 1, 2, 3, 800]
lista[3] = 300
print('Mudando elementos da lista:', lista)

print('\n')

#listas aninhadas
lista = [1,5,7,8],[5,8,9],[9,6,3,0]
print(lista)
print('Listas aninhadas:', lista)

print('\n')

# Somando listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

total = lista1 + lista2
print('Somando listas:', total)

print('\n')

# index() localiza e informa o índice do elemento
lista = [0, 1, 2, 3, 800]
print(lista)
print('Posição do 800:', lista.index(800))

print('\n')

# reverse() inverte elementos da lista
lista = [0, 1, 2, 3]
lista.reverse()
print('Lista Invertida:', lista)

print('\n')

#função sort ordena a lista
lista = [3, 1, 2, 0]
lista.sort()
print('Lista em ordem:', lista)

# Parâmetro 'reverse=True' inverte
lista = [1,2,3,4,5,6,7,8,9]
lista.sort(reverse=True)
print(lista)

