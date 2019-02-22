

class Pessoa:

    # Método de inicialização:
    def __init__(self, nome, idade, peso, altura):
        # Nome, idade, peso e altura são os parâmetros
        # E também são os atributos do objeto
        
        # *SELF* faz referência ao objeto que 'chamou' a classe/método
        self.nome   = nome  # Dando os valores às caract. do objeto
        self.idade  = idade
        self.peso   = peso
        self.altura = altura
        
        
    # Definido um Método
    def mostrarDados(self):
            # Sempre precisa passar o parâmetro self
            # Pois é o objeto que chama o método/função


        texto = '''
        {0} tem {1} anos de idade, pesa {2} Kg e tem {3} m de altura. \n'''

        # Exibe todas as informaçõs da pessoa (objeto)
        print(texto.format(self.nome, self.idade, self.peso, self.altura))

    # Método que checa se a pessoa é de maior
    def maioridade(self):

        if self.idade < 18:
            print('{} é menor de idade'.format(self.nome))
        
        else:
            print('{} é maior de idade'.format(self.nome))
    
    # Definido Método da classe que mostra o imc
    def mostrarIMC(self):

        # Cálculo do imc guardado numa variável
        imc  = self.peso / (self.altura**2) 
        
        # Para evitar escrever várias vezes a mesma coisa
        nome = self.nome
        texto = ' você está na faixa: '

        print('Seu IMC é: ' + str(imc))
        
        # Checa a faixa que o IMC da pessoa(Objeto) está
        if imc > 40:
            print(nome + texto + 'Obesidade III (Morbida)')

        elif imc > 35:
            print(nome + texto + 'Obesidade II (Severa)')

        elif imc > 30:
            print(nome + texto + 'Obesidade I')

        elif imc > 25:
            print(nome + texto + 'Acima do Peso')

        elif imc > 18.5:
            print(nome + texto + 'Peso Normal')

        elif imc > 17:
            print(nome + texto + 'Abaixo do peso')
        
        else:
            print(nome + texto +  'Muito Abaixo do Peso')    

    pass