# Importando a biblioteca tkinter e todos os seus modulos
from tkinter import *

# Criando a janela principal da aplicação através de classe Tk()
# criando uma instância da classe Tk()
janela = Tk()

# Criando uma função para quando o 1° botão for clicado, 
# ele pegue o nome que foi digitado na caixa de texto através do método 'get'
# e então substitua essa mensagem no nosso 'label' usando a propriedade 'text'
def Muda_nome():
    lb2['text'] = caixa_texto.get()

# criando uma função para quando o 2° botão for clicado ele voltar 
# a exibir a primeira menssagem 'Seu nome aqui !'
def Voltar():
    lb2['text'] = 'Seu nome aqui !'

# Label, atribuindo ele a janela principal, definindo a largura como 30px,
# definindo o seu texto e definindo a fonte do texto
lb = Label(janela, width=30, text='Digite o seu nome', font=('arial', 20, 'bold'))

# Gerenciador de layout 'place', nos definimos as coordenadas do nosso label na janela
# x: distância da margem esquerda para o centro
# y: distância do topo da margem para o centro
lb.place(x=-65, y=70)

# Entrada de texto com o widget Entry, com largura de 20px
caixa_texto = Entry(janela, width=20)
caixa_texto.place(x=125, y=140)

# criando um botão com o widget Button, atribuindo ele a janela principal, definindo a largura como 30px,
# Button(janela, largura, altura, texto_exibido, cor_de_fundo, fonte(fonte, tamanho, estilo) , função_do_botão)
btn1 = Button(janela, width=20, height=2, text='Clique aqui', bg='red', font=('arial', 10, 'bold'), command=Muda_nome)
btn1.place(x=105, y=180)

btn2 = Button(janela, width=20, height=2, text='Voltar', bg='green', font=('arial', 10, 'bold'), command=Voltar)
btn2.place(x=105, y=250)

lb2 = Label(janela, width=30, text='Seu nome aqui !', font=('arial', 20 , 'bold'))
lb2.place(x=-65, y=330)

# Definindo tamanho e posição da janela criada
janela.geometry('400x400+400+150')
# Largura x Altura + Distância da margem esquerda da tela + Distância em releção ao topo da tela 

# title() : Define o titulo da janela
janela.title('Exemplo 1')

# Método que faz com que a janela fique sendo exibida na tela
janela.mainloop()




















