
class Banco():

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    # Métodos da Classe Banco
    def exibir_saldo(self):
        print(self.saldo)

    def retornar_saldo(self):
        return self.saldo
    
    pass

conta = Banco("Lucas", 2000)

# Duas formas de exibir o saldo
conta.exibir_saldo()

saldo = conta.retornar_saldo()
print(saldo)



# Colocar valores default no Método Construtor
# Criar métodos de saque e depósito
