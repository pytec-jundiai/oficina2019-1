
class Banco():

    def __init__(self, nome, saldo=2000):
        self.nome = nome
        self.saldo = saldo
        self.aberta = True

    def alterar_conta(self):
        self.aberta = not self.aberta

    def exibir_info(self):
        estado = 'aberta' if self.aberta else 'fechada'
        print(f' Nome: {self.nome} \n Saldo: R${self.saldo} \n Conta {estado}')

    def exibir_saldo(self):
        print(f'Seu Saldo atual: R${self.saldo}')
  
    def depositar(self, valor):
        if self.aberta:
            self.saldo += valor
            self.exibir_saldo()
        else:
            print('Conta Fechada!!')

    def sacar(self, valor):
        if self.aberta:
            self.saldo -= valor
            self.exibir_saldo()
        else:
            print('Conta Fechada!!')


    pass




