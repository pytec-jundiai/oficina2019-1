'''
Manipúlação de textos
'''

teste = 'Programar em Python é Muito Legal e Divertido! '

	# Verificação

# Verifica quantos caracteres a string possui
exemplo = len(teste)
print('Caracteres: ', exemplo) 

# count() conta quantas vezes uma determinada string aparece na frase
exemplo = teste.count('a')
print('Letra a aparece: ', exemplo)
exemplo = teste.count('Python')
print('Palavra Python aparece: ', exemplo)

#find() informa posição da string procurada
print('Palavra procurada está no: ', teste.find('Muito'))

# in verifica se a palavra 'legal' está dentro da String 'teste'
exemplo = 'legal' in teste
print(exemplo)

	#Transformação
print('\n')
# replace() troca uma string por outra
exemplo = teste.replace('Legal','BOMMM')
print(exemplo)

# upper() transforma todas as letras da String em maiúsculas
exemplo = teste.upper()
print(exemplo)

# lower() coloca todas as letras em minúsculas
exemplo = teste.lower()
print(exemplo)

# capitalize() deixa toda a frase em minúsculo, menos primeira letra
exemplo = teste.capitalize()
print(exemplo)

# title() deixa a primeira letra de cada palavra em maiúsculo
print('Título: ', teste.title())

#A função Strip retira os espaços antes e depois da string
exemplo = '     Casa Amarela      '
print(exemplo)
print(exemplo.strip())


	# Divisao & Junção
print('\n')

# split() divide a string com base nos espaços entre as palavras 
# criando uma lista com cada palavra em um índice
exemplo = teste.split()
print(exemplo)

# join() ideal para juntar listas
print('-'.join(exemplo))


	#Fatiamento
print('\n')

# O fatiamento de string é realizado atravez dos []
# temos um padrão a ser seguido

# Início da frase a ser fatiada : Até aonde a frase vai ser fatiada : parâmetro para o fatiamento]
# ex: 0:10:2

# Pega apenas a letra que esta na posição 3
fatiamento = 'Eu vou ser a frase fatiada '
print(fatiamento[3])

# Seleciona a letra na posição 3 e até o final da frase
print(fatiamento[3:])

# Nenhum parametro antes dos ':' logo ele exibe a letra na posição 0 até a 8
print(fatiamento[:8])

# Neste exemplo não é informado nada, 
# logo ele pega da letra na posição 0 até o final da frase
print(fatiamento[:])

# Neste exemplo pula-se de 2 em 2 e a cada pulo é retorna apenas uma letra
print(fatiamento[::2])

# Similar ao exemplo de cima, o pulo é de 2 em 2,
# porém estou indo da posição 0 a posição 10 da frase
print(fatiamento[0:10:2])