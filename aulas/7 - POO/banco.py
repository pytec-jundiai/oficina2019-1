class Banco:

    def __init__(self,nome,saldo,numero_conta,nome_banco):

        self.nome = nome
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_banco = nome_banco

    def mostra_dados(self):

        print(f'''Nome do cliente: {self.nome}
Saldo: {self.saldo}
Numero da conta: {self.numero_conta}
Nome do banco {self.nome_banco}''')

    def sacar(self):
        valor = float(input('Digite o valor do saque: '))
        self.saldo -= valor

    def depositar(self):
        valor = float(input('Digite o valor do depósito: '))
        self.saldo += valor


    def verifica_saldo(self):
        print('Saldo Atual: R$', self.saldo)



