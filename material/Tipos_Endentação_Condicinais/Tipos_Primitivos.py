'''
Tipos dispon�veis em python:

- int
- float
- bool
- str (string)

Em python �s vari�veis s�o tipidas dinamicamente, significa que o seu tipo � determinado
pelo dado que recebe.

O M�todo utilizado  para converter em python � chamado de 'Cast'.
'''

# Rebendo dados em python em uma vari�vel
nome = input('Digite o seu nome:') # por padr�o, o input retorna str.

# imprimindo o nome na tela
print(nome)


# Caso queira receber um n�mero inteiro do usu�rio
numero = int(input('Digite sua idade:')) # estou convertendo o retorno do input de str para int


# N�mero com ponto flutuante ou decimal
peso = float(input('Digite o seu peso:'))



# Trabalhando com o tipo bool
teste = bool(input('Digite algo: ')) # se houver conte�do(algum tipo de dado) ser� armazenado True, sen�o False.
print(teste)

'''
  - - - Convers�es de tipos num�ricos
'''

n1 = 249
n2 = float(n1) 
print(n2)

# Caso queira converter de float para inteiro
peso = 123.5

pesointeiro = int(peso) # O python vai ignorar todos os n�meros ap�s o ponto.

print(pesointeiro)