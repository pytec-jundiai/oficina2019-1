#Importando a biblioteca tkinter e todos os seus modulos
from tkinter import *

#criando a janela principal da aplicação através de classe Tk()
#criando uma instância da classe Tk() a atribuindo a mesma na variavel 'janela'
janela = Tk()

#criando uma função para quando o 1° botão for clicado, ele pegue o nome que foi digitado na caixa de texto através do método 'get'
#e então substitua essa mensagem no nosso 'label' usando a propriedade 'text'
def Muda_nome():
    lb2['text'] = caixa_texto.get()

#criando uma função para quando o 2° botão for clicado ele voltar a exibir a primeira menssagem 'Seu nome aqui !'
def Voltar():
    lb2['text'] = 'Seu nome aqui !'

#criando um label com o widget Label, atribuindo ele a janela principal, definindo a largura como 30px,
#definindo o seu texto e definindo a fonte do texto
lb = Label(janela, width=30, text='Digite o seu nome', font=('arial', 20, 'bold'))

#usando o gerenciador de layout 'place', nos definimos as coordenadas do nosso label na janela
#x: distância da margem esquerda para o centro/y: distância do topo da margem para o centro
lb.place(x=-65, y=70)

#criando uma caixa de texto com o widget Entry, atribuindo ele a janela principal e definindo a largura como 20px
caixa_texto = Entry(janela, width=20)
caixa_texto.place(x=125, y=140)

#criando um botão com o widget Button, atribuindo ele a janela principal, definindo a largura como 30px,
#definindo o seu texto, definindo a cor de fundo do botão e definindo a fonte do texto
#o parametro command está recebendo a função que foi criada, ao pressionar o botão ele executa a ação
btn1 = Button(janela, width=20, height=2, text='Clique aqui', bg='red', font=('arial', 10, 'bold'), command=Muda_nome)
btn1.place(x=105, y=180)

btn2 = Button(janela, width=20, height=2, text='Voltar', bg='green', font=('arial', 10, 'bold'), command=Voltar)
btn2.place(x=105, y=250)

lb2 = Label(janela, width=30, text='Seu nome aqui !', font=('arial', 20, 'bold'))
lb2.place(x=-65, y=330)

#aqui estamos definindo o tamanho da janela que será criada atravez do método geometry
janela.geometry('400x400+400+150')

#1° medida (400): Largura da janela
#2° medida (400): Altura da janela
#3º medida (400): Medida em pixels da janela na tela da margem esquerda com relação ao centro
#4º medida (150): Medida em pixels da janela na tela do topo com relação ao centro

#Definindo o titulo da janela através do método 'title'
janela.title('Exemplo 1')

#método que faz com que a janela fique sendo exibida na tela
janela.mainloop()




















