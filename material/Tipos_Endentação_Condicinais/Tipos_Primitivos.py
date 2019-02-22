'''
Tipos disponíveis em python:

- int
- float
- bool
- str (string)

Em python às variáveis são tipidas dinamicamente, significa que o seu tipo é determinado
pelo dado que recebe.

O Método utilizado  para converter em python é chamado de 'Cast'.
'''

# Rebendo dados em python em uma variável
nome = input('Digite o seu nome:') # por padrão, o input retorna str.

# imprimindo o nome na tela
print(nome)


# Caso queira receber um número inteiro do usuário
numero = int(input('Digite sua idade:')) # estou convertendo o retorno do input de str para int


# Número com ponto flutuante ou decimal
peso = float(input('Digite o seu peso:'))



# Trabalhando com o tipo bool
teste = bool(input('Digite algo: ')) # se houver conteúdo(algum tipo de dado) será armazenado True, senão False.
print(teste)

'''
  - - - Conversões de tipos numéricos
'''

n1 = 249
n2 = float(n1) 
print(n2)

# Caso queira converter de float para inteiro
peso = 123.5

pesointeiro = int(peso) # O python vai ignorar todos os números após o ponto.

print(pesointeiro)