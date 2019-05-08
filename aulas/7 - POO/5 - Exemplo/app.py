from banco import *


menu = '''
Escolha a opção desejada
    1 - Fechar/Abrir Conta
    2 - Depositar
    3 - Sacar
    4 - Exibir Informações da Conta
    5 - Sair
    '''

nome = input('Digite o Nome: ')
conta = Banco(nome)

while True:

    print(menu)
    opcao = int(input('::'))

    if opcao == 1:
        conta.alterar_conta()
    
    elif opcao == 2:
        valor = float(input('Depósito: '))
        conta.depositar(valor)
        
    elif opcao == 3:
        valor = float(input('Depósito: '))
        conta.sacar(valor)
        
    elif opcao == 4:
        conta.exibir_info()

    elif opcao == 5:
        break