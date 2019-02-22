from tkinter import * #importando a biblioteca tkinter e todas as suas funcionalidades

#função que soma, estou pegando o texto dela atravez da função get e atribuindo
#ao label 'lb_result' que foi criado atravez da propriedade 'text'
def soma():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = num1 + num2

#função que subtrai, estou pegando o texto dela atravez da função get e atribuindo
#ao label 'lb_result' que foi criado atravez da propriedade 'text'
def subtracao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = num1 - num2

#função que multiplica, estou pegando o texto dela atravez da função get e atribuindo
#ao label 'lb_result' que foi criado atravez da propriedade 'text'
def multiplicacao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = num1 * num2

#função que divide, estou pegando o texto dela atravez da função get e atribuindo
#ao label 'lb_result' que foi criado atravez da propriedade 'text'
def divisao():
    num1 = int(n1.get())
    num2 = int(n2.get())
    lb_result['text'] = ('{:.2f}'.format(num1 / num2))

#criando a janela principal atravez da classe Tk
janela = Tk()

#Criando uma caixa de etxto atravez do widget Entry
n1 = Entry(janela,font=('arial',12,'bold'))
n1.place(x=350,y= 50)

#Criando uma caixa de etxto atravez do widget Entry
n2 = Entry(janela,font=('arial',12,'bold'))
n2.place(x=350,y=90)

#Criando um botão e atribuindo ele a variavel 'btn_soma'
btn_soma = Button(janela, width= 20, bg='blue', text='Soma',font=('arial', 15, 'bold'), command=soma)
btn_soma.place(x=120,y=330)

#Criando um botão e atribuindo ele a variavel 'btn_sub'
btn_sub = Button(janela, width= 20, bg='red', text='Subtração',font=('arial', 15, 'bold'), command=subtracao)
btn_sub.place(x=120,y=280)

#Criando um botão e atribuindo ele a variavel 'btn_mult'
btn_mult = Button(janela, width= 20, bg='yellow',text='Multiplicação',font=('arial', 15, 'bold'), command=multiplicacao)
btn_mult.place(x=120,y=230)

#Criando um botão e atribuindo ele a variavel 'btn_divi'
btn_divi = Button(janela, width= 20,bg='pink', text='Divisão',font=('arial', 15, 'bold'), command=divisao)
btn_divi.place(x=120,y=180)

#criando um Label onde será atribuido o resultado das operações
lb_result = Label(janela,text='Resultado', font=('arial', 20 , 'bold'))
lb_result.place(x=190, y=400)

#Label criado para mostrar a mensagem 'Digite um numero'
lb_text = Label(janela, text='Digite um numero', font=('arial', 20 , 'bold'))
lb_text.place(x=30,y=40)

#Label criado para mostrar a mensagem 'Digite um numero'
lb_text2 = Label(janela, text='Digite um numero', font=('arial', 20 , 'bold'))
lb_text2.place(x=30,y=90)

#Definindo o tamanho da janela
janela.geometry('500x500+150+150')

#Mantem a janela sendo exibida
janela.mainloop()
























