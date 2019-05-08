
class Banco():

    def __init__(self, nome, saldo=2000):
        self.nome = nome
        self.saldo = saldo

    def exibir_saldo(self):
        print(f'Seu Saldo atual: R${self.saldo}')
  
    def depositar(self, valor):
        self.saldo += valor
        self.exibir_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.exibir_saldo()

    pass


# Criar novo atributo conta aberta
# criar método para exibir todas informações
# implementar lógica da conta aberta/fechada nos outros métodos
# Criar no app um programa básico usando poo