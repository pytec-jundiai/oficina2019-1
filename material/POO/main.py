# Importando a classe criada 
from pessoa import *

opcao = 1

menu ='''
[1] - Inserir Outros Dados
[2] - Mostrar Dados
[3] - Checar se é maior de idade
[4] - Mostrar IMC
[5] - Sair (x)
'''

while opcao != 5:

    if opcao == 1:
        
        # Inserindo os valores dos atributos
        nome    = input('Digite o Nome: ')
        idade   = int(input('Digite a Idade: '))
        peso    = int(input('Digite seu peso (kg): '))
        altura  = float(input('Digite sua altura (metros) : '))
        
        # Criando um objeto:
        p1 = Pessoa(nome, idade, peso, altura) 
                    # Passa-se os parâmetros também

    elif opcao == 2:
        # Objeto chamando o método da classe Pessoa
        p1.mostrarDados()

    elif opcao == 3:
        p1.maioridade()

    elif opcao == 4:
        p1.mostrarIMC()

    
    print(menu)
    opcao = int(input('Escolha uma opção: '))
    print('\n')