'''

MATERIAL DE APOIO : GUI - Graphics User Interface

Definição de alguns conceitos que serã oabordados:

    Widget: Um componente que compoem uma interface grafica Ex: Botoes,caixa de texto, etc.
    Container: É um widget que pode conter outros widgets e é capaz de conter outros objetos dentro

    Label: É um widget que cria uma texto na tela, voce pode posiciona-lo atravez dos gerenciadores
    de leyalt

    Botão: Um widget da biblioteca tkinter que ao ser criado, executa alguma determinada ação que
    foi pré definida atravez da criação de uma função.

    Entry: É um widget que cria um campo de texto na tela, é possivel capturar o conteudo que foi digitado
    dentro dele.



'''



'''Estamos criando uma janela com um botão'''


#aqui estou importando a biblioteca tkinter e todas as suas funcionalidades
from tkinter import *

janela = Tk() #Tk é a classe que retorna a instancia (a representação) da janela principal
#a variavel 'janela' vai adiquirir a referencia da janela principal que foi criado

#aqui estou criando um botão
#btn_click está recebendo a instancia(representação) do widget Button, que está vinculado a janela principal
btn_click = Button(janela, width= 20, text='Botao de Teste')#width: tamanho do botao, que é de 20 pixels

#place é um gerenciador de leyalt do tkinter, com o x e y definimos aonde a janela vai aparecer
btn_click.place(x = 85, y = 130)
#x: distancia da magem esquerda para o centro/y: distancia do topo da margem para o centro

#aqui estamos definindo o titulo da janela atravez da função tittle
janela.title('Teste')

#bg significa back ground (é o fundo da janela), estamos alterando a cor de fundo da janela
janela['bg'] = 'Green'

#aqui estamos definindo o tamanho da janela que será criada atravez da função geometry
janela.geometry('300x300+400+150')

#função que faz a janela fique sendo exibida na tela
janela.mainloop()

#------------------------------------------------------------------------------------------------------------


'''Estamos criando uma janela que ao ser clicado, o texto que está nela é mudado'''

from tkinter import *

#definindo uma função para quando o botao for clicado exibir uma mensagen na tela
def bt_click():
    lb['text'] = 'Teste'#'text' é uma propriedade do tkinter, como a função esta vinculada ao botao,quando o botao for
#clicado, ele substituira o a mensagem do label pela mensagem 'Teste'
#Basicamente estamos dizendo ao python que quando o botao for clicado para substituir a mensagem do label pela mensagem que foi definida

#aqui está ocorrendo a mesma coisa que no caso acima
def bt_click2():
    lb['text'] = 'Label'

janela = Tk()


#criando um botão e colocando ele dentro da variavel bt1 / width: é a largura do botão
bt1 = Button(janela, width=20, text= 'Clique no Botão', command=bt_click)#estamos vinculando a função bt_click ao atributo command
bt1.place(x=85,y=130)

#criando um botão e colocando ele dentro da variavel bt2
bt2 = Button(janela, width=20, text='Voltar',command=bt_click2)
bt2.place(x=85,y=170)

#aqui estamos criando um label atravez do widget 'Label', ou seja, uma caixa de texto com um texto já pré definido
lb = Label(janela,width=20, text='Label', font=('arial',20, 'bold'))
lb.place(x=1,y=80)

#aqui estamos definindo o titulo da janela atravez da função tittle
janela.title('Teste 02')

#estamos definindo o tamanho da janela
janela.geometry('300x300+200+200')

#mantem a janela sendo exibida
janela.mainloop()


