# Módulos usados
from random import randint
from time import sleep

# índices: 0       1        2
opcao=['Pedra', 'Papel', 'Tesoura']

menu='''
    Jo Ken Po

 [ 1 ] Pedra
 [ 2 ] Papel
 [ 3 ] Tesoura

 [ 4 ] Sair
'''
jogador = 0

while jogador != 4:
    
    print(menu)
    
    # Jogador Escolhe
    jogador = int(input('Escolha: '))
    
    # Escolhe um número aleatório de 1 à 3
    computador = randint(1,3)
                           
    # Sai do jogo
    if jogador == 4:
        break # Break finaliza o loop (while)

    # Mostra a opção do Jogador
    print('\n','Você escolheu: ', opcao[jogador-1])
    # -1 pois índice começa no 0 e o jogador escolhe de 1 à 3
    # sendo que a lista 'opcao' vai de 0 à 2
    
    print('\t'*4+'Jo') # '\t'*4 = tab 4 vezes
    sleep(1) # Pausa por 1 s o programa
    print('\t'*4+'Ken')
    sleep(1)
    print('\t'*4+'Po')
    sleep(1) 

    # Mostra a opção do Computador                        
    print('Computador Escolheu: ', opcao[computador-1],'\n'*2) #'\n'*2 = enter 2 vezes
    # -1 pois índice começa no 0
    

    if jogador == computador: # Jogador e Computador escolhem mesmo número
        print('Empate!')

    elif jogador == 1 and computador == 2: # Jogador: Pedra / PC: Papel
        print('Computador Ganhou!')

    elif jogador == 1 and computador == 3: # Jogador: Pedra / PC: Tesoura
        print('Jogador Ganhou!')

    elif jogador == 2 and computador == 1: # Jogador: Papel / PC: Pedra
        print('Jogador Ganhou')

    elif jogador == 2 and computador == 3: # Jogador: Papel / PC: Tesoura
        print('Computador Ganhou!')

    elif jogador == 3 and computador == 1: # Jogador: Tesoura / PC: Pedra
        print('Computador Ganhou')

    elif jogador == 3 and computador == 2: # Jogador: Tesoura / PC: Papel
        print('Jogador Ganhou!')

print('Até a próxima..')