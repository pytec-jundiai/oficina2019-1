from banco import *

opcao = 1

menu =  ('''

     Escolha a opção desejada
        1 - Entrar com novos dados
        2 - Sacar
        3 - Depositar
        4 - Verificar Saldo
        5 - Sair
    ''')

while opcao != 5:

    if opcao == 1:
        nome = input('Digite o Nome: ')
        saldo = float(input('Digite o seu saldo:  '))
        numero_conta = int(input('Digite o numero da sua conta: '))
        nome_banco = str(input('Digite o nome do seu banco: '))
        print()

        first = Banco(nome,saldo,numero_conta,nome_banco)
        first.mostra_dados()


    elif opcao == 2:
        first.sacar()

    elif opcao == 3:
        first.depositar()

    elif opcao == 4:
        first.verifica_saldo()

    print(menu)
    opcao = int(input('Escolha uma opção: '))
