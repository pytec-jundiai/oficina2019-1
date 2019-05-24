from tkinter import *

# Operações
def adicao():
    # get(): Recebe os valores dos Entry
    num1 = int(n1.get())
    num2 = int(n2.get())
    # Altera o valor do label text para a resultado da operação
    # através da propriedade 'text'
    lb_result['text'] = num1 + num2

def subtracao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = num1 - num2

def multiplicacao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = num1 * num2

def divisao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = ('{:.2f}'.format(num1 / num2))

# Cria janela principal
janela = Tk()

# Entry: cria uma caixa de entrada
n1 = Entry(janela)
n1.place(x=350,y= 50)

n2 = Entry(janela)
n2.place(x=350,y=90)

# Criando um botão e atribuindo ele a função adição
btn_soma = Button(janela, width= 20, bg='blue', text='Soma',font=('arial', 15, 'bold'), command=adicao)
btn_soma.place(x=120,y=330)

# Criando um botão e atribuindo ele a função subtração
btn_sub = Button(janela, width= 20, bg='red', text='Subtração',font=('arial', 15, 'bold'), command=subtracao)
btn_sub.place(x=120,y=280)

# Criando um botão e atribuindo ele a função multiplicação
btn_mult = Button(janela, width= 20, bg='yellow',text='Multiplicação',font=('arial', 15, 'bold'), command=multiplicacao)
btn_mult.place(x=120,y=230)

# Criando um botão e atribuindo ele a função divisão
btn_divi = Button(janela, width= 20,bg='pink', text='Divisão',font=('arial', 15, 'bold'), command=divisao)
btn_divi.place(x=120,y=180)

# Label onde será atribuido o resultado das operações
lb_result = Label(janela,text='Resultado', font=('arial', 20 , 'bold'))
lb_result.place(x=190, y=400)

#Label criado para mostrar a mensagem 'Digite um numero'
lb_text = Label(janela, text='Digite um numero', font=('arial', 20 , 'bold'))
lb_text.place(x=30,y=40)

# Label criado para mostrar a mensagem 'Digite um numero'
lb_text2 = Label(janela, text='Digite um numero', font=('arial', 20 , 'bold'))
lb_text2.place(x=30,y=90)

# Definindo o tamanho da janela
janela.geometry('500x500+150+150')

# Mantem a janela sendo exibida
janela.mainloop()

















