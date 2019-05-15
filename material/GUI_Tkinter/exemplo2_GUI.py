from tkinter import *

janela = Tk()

#criando funções para alterar a cor de fundo da janela principal através da propriedade 'bg' (background)
def Red():
    janela['bg'] = 'red'

def Green():
    janela['bg'] = 'green'

def Blue():
    janela['bg'] = 'blue'

def Yellow():
    janela['bg'] = 'yellow'

'''
Criamos 4 botões e a cada um atribuimos a função através do parâmetro 'command' para quando os mesmos forem clicados
eles realizarem as ações que foram programados  (mudar a cor de fundo da janela)
'''

btn1 = Button(janela, width=3,height=1,bg='red', font=('arial', 10, 'bold'), command=Red)
btn1.place(x=180, y=60)

btn2 = Button(janela, width=3,height=1,bg='green', font=('arial', 10, 'bold'), command=Green)
btn2.place(x=50, y=180)

btn3 = Button(janela, width=3,height=1,bg='blue', font=('arial', 10, 'bold'), command=Blue)
btn3.place(x=320, y=180)

btn4 = Button(janela, width=3,height=1,bg='yellow', font=('arial', 10, 'bold'), command=Yellow)
btn4.place(x=180, y=320)

janela.title('Exemplo 2')
janela.geometry('400x400+400+150')

janela.mainloop()







