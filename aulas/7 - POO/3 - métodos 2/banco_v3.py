
class Banco():

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def exibir_saldo(self):
        print(f'Seu Saldo atual: R${self.saldo}')

    # Novos Métodos Implementados
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    pass

conta = Banco("Lucas", 2000)
conta.exibir_saldo()

conta.depositar(1000)
conta.exibir_saldo()

conta.sacar(1000)
conta.exibir_saldo()

# Colocar método exibir_saldo() 
# dentro dos outros métodos