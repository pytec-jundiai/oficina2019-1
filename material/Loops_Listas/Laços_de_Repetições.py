
# Laços de Repetição

'''Os laços de repetição no python sao representados com o comando 'for' e 'while'
    
   Vou explicar para vocês usando exemplos
   
   Mas primeiro vamos entender a diferença os dois:
   
   Laço for: É sugerido usar o for loop nas seguintes circunstãncias:

    *Você tem em mente a quantidade de vezes em que deseja que um bloco de código seja repetido
    *Você quer controlar, o número de vezes em que a tarefa será executada
    *A tarefa se repetirá por um número de vezes finito e predefinido
   
   Laço while: Já o while loop é sugerido nos seguintes casos:

    *Você não faz a menor ideia de quantas vezes um bloco de código deverá ser executado
    *Quando não lhe cabe predefinir quantas vezes uma determinada tarefa deverá ser executada.
    *O bloco de código, em questão, deverá se repetir infinitamente, enquanto uma condição não for satisfeita.
'''
#Estrutura de repetição for

nomes = ['Pedro', 'João', 'Leticia'] #foi declarado uma lista com nomes
for n in nomes:
    print(n)

'''
A variável 'nomes' é uma lista inicializada com uma sequência de valores 
do tipo string. A instrução for percorre todos esses elementos, um por vez e 
em cada loop, atribui o valor do item a variável n, que é impressa em seguida. 
O resultado, então, é a impressão de todos os nomes contidos na lista. 
'''
print('\n')

#----------------------------------------------------------------------------------------------------

#estrutura de repetição while

#Programa simples usando while que faz uma contagem de 0 até  10

cont = 0
while cont < 10: #ao usar o while é necessario inicializar a variavel que será o contador pois caso contrario ocorrera um erro
    cont += 1 #mesma coisa que cont = cont + 1
    print(cont) #a cada loop a variavel que foi incrementada (cont) é exibida com seu novo valor

'''
O comando while, por sua vez, faz com que um conjunto de instruções seja executado 
enquanto uma condição for atendida. Quando o resultado passa a ser falso, 
a execução é interrompida, saindo do loop, e passa para o próximo bloco.

No código a cima, vemos um exemplo de uso do laço while, 
onde definimos a variável contador,e iniciando com 0, 
e enquanto seu valor for menor que 10, executamos as instruções.

A parte do 'cont += 1' esta sendo usada como um delimitador, ou seja, 
uma variavel de controle para que o laço nao seja infinito, ele vai indicar
ao while a hora de interromper o loop, a cada loop a variavel cont é incrementada, ou seja,
a cada loop é adicionado +1, e quando esse valor for menor do que 10, que é a condição
que foi estabelecida, o loop é interrompido e exibido o resultado final.
'''

print('\n')

#---------------------------------------------------------------------------------------------------

#Outro exemplo da estrutura for

for c in range(1,11):#É a mesma coisa que: faça o contador percorrer o laço no intervalo de 1 a 10
    print(c)

'''Vamos entender o que está acontecendo: a variacel 'c' está percorrendo todo
o laço e a cada loop é armazenado um numero nele que logo em seguida é exibido no print.
A função 'range' significa: no intervalo de. Note que foi colocado de 1 a 11 e nao de 1 a 10
pois ele sempre para um numero antes, faça seus testes e mude 11 para 10'''

#----------------------------------------------------------------------------------------------

#exemplo usando o for para percorrer uma lista

lista = ['a','b','c','d','e']  #declarando uma lista de letras

for c in lista:  #declaramos uma variavel c que será o nosso contador
    print(c)

'''A variavel c está percorrendo a lista, ou seja, ela está dentro de um loop
onde a cada loop uma letra da lista que foi declarada é armazenada na variavel 'c'
e depois é exibida no print, o 'in' significa neste contexto: dentro da lista, ou seja,
faça a variavel 'c' percorrer dentro da lista e depois exibir o seu conteudo no print
 '''


#--------------------------------------------------------------------------------------------

'''aqui temos um programa um pouco mais elaborado onde o usuario digita uma quantidade x
de numeros a serem somados e logo em seguida digita os numeros que vao ser somados'''

n1 = int(input('Digite a quantidade de numeros a serem somados: '))
soma = cont = 0
while cont < n1:
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
print(f'A soma dos valores é de {soma}')

'''
O programa soma uma quantidade x de numeros que é informado logo no inicio do codigo
entao o laço de repetição é executado, enquanto o cont for menor que o n1 (n1: quantos numeros 
vão ser somados) faça o que está dentro do laço, logo em seguida é pedido os numeros que vao ser
somados, a variavel 'soma' tem o papel de armazenar e somar todos os numeros que foram digitados
para depois ser exibido o resultado final no print.
'''
print('\n')
#-----------------------------------------------------------------------------------------------------------

#Exemplo de while usando strings


palavra_igual = ' '
while palavra_igual != 'oi'.strip():
    palavra_igual = input('Me da um oi: ')

'''
Aqui temos um exemplo da estrutura de repetição while sendo usado com strings
Enquanto a palavra que for digitada for diferente de 'oi' , ele continuara pedindo
para o usuario 'dar um oi', repare que a variavel 'palavra_igual' foi inicializada apenas
com aspas simples, ou seja, vazia,pois o valor esperado de retorno é do tipo 'str'
caso contrario o codigo exibiria um erro de tipos de valores.
'''