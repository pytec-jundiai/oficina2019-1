# Dicionários

# Criando um:
dict1 =	{
  'marca': 'Ford',
  'modelo': 'Mustang',
  'ano': 1964
}
print(dict1, '\n')

# copy() retorna uma cópia do dicionário
dict2 = dict1.copy()
print('Dicionário copiado:', dict2)

# clear() remove todos os elementos do dicionário
dict2.clear()
print('Dicionário 2 apagado:', dict2, '\n')

# fromkeys() cria um dicionário com as chaves e valores especificados
chaves = ('k1','k2', 'k3')
valores = 10
dict2 = dict.fromkeys(chaves, valores)
print('Dicionário criado: ',dict2)

# get() retorna o valor de uma determinada chave
valor = dict1.get('marca')
print('Valor da chave marca:', valor, '\n')

# items() retorna uma lista com tuplas contendo chave e seu valor
for tuplas in dict1.items():
	print('Chave e Valor:', tuplas)

print('\n') 

# keys() retorna uma lista contendo todas as chaves do dicionário
chaves = dict1.keys()
print('Chaves do Dicionário', chaves, '\n')

dict2 = dict1.copy()
# pop() remove elemento de uma especificada chave
dict2.pop('marca')
print('Deleta a chave marca e seu valor', dict2, '\n')

# popitem() remove o último par de chave e valor
dict2.popitem()
print('Deleta ultíma chave e seu valor', dict2, '\n')

# setdefault() retorna o valor da chave, caso não exista será criada
# Com chave já criada:
valor = dict1.setdefault('modelo','Mustang')
print('Valor da chave existente:', valor)

# Com chave não criada:
valor = dict1.setdefault('cor', 'Preto')
print('Valor da inexistente:', valor, '\n')

# update() insere par de {chave : valor}
dict1.update({'estado':'Novo'})
print('Após comando update:', dict1, '\n')

# values() retorna uma lista com todos os valores do dicionário
valores = dict1.values()
print(valores, '\n')
# Pode ser feito assim:
for valor in dict1.values():
	print(valor)
