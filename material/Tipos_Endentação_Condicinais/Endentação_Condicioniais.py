'''
Endentação:
	É o recuo de um texto em relação à sua margem
	Python por não utilizar '{}' usa endentação realizar sua execução

Condicionais:
	Testes lógicos

'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

# Caso teste lógico seja verdadeiro, execute o print
if a < b:
	print('a é menor que b')
	'''
	Observe o recuo da margem, isso mostra que o comando print
	faz parte do 'if'
	'''
# Excuta caso teste lógico seja verdadeiro 
# e apenas quando o anterior já tenha ocorrido
elif a > b:
	print('a é maior que b')

# Excuta caso todos os testes lógicos anteriores derem falso
else:
	print('a é igual a b')