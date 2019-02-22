'''
Definição de função:

Na programação, funções são blocos de código que realizam determinadas
tarefas que normalmente precisam ser executadas diversas vezes dentro de uma aplicação.
'''

def linha(): #criamos uma função usando a palavra reservada def
    print('-=-'*30) #essa função exibi uma linha ao ser chamada
    print('Esta função criou duas linhas '.center(80)) #center é um metodo que centraliza strings
    print('-=-' * 30)

linha() #para a função ser executada é necessario chama-la


'''
Parametros de funçoes:
    
    Ao criar uma função pode-se estabelecer parametros para a mesma,
    quando a função for chamada, tais parametros devem ser atendidos.
    
'''

def soma(n1,n2):    #estou criando uma função que soma dois numeros, o n1 e o n2 sao os parametros
    s = n1 + n2     #ou seja, é necessario digitar dois numeros para a função ser executada
    print(f'A soma entre {n1} e {n2} é de {s}')

soma(4,6) #estou chamando a função e pedindo para que ela some 4 + 6 e exiba o resultado



def carinhas(): #aqui estou criando uma função mais elaborada que exibe carinhas
    cara = input('Digite Feliz/Felizao/Triste/Mau ou Surpreso: ').upper().strip()
    if cara == 'FELIZ':
        print(':)')
    elif cara == 'FELIZAO':
        print(':D')
    elif cara == 'TRISTE':
        print(':(')
    elif cara == 'MAU':
        print('>:)')
    elif cara == 'SURPRESO':
        print(':O')

carinhas()

'''
Parametros Opicionais:

    Parametros opicionais, como o proprio nome já diz, sao parametros que podem ou nao
    ser atendidos, ou seja, eles sao opicionais, vamos criar uma função que multiplica
    e usar osp arametros opicionais.
'''

def multi(n1,n2,n3=1): #estou definindo 3 parametros mas repare que eu defini o n3 com o valor 1
    m = n1 * n2 * n3   #na multiplicação o valor nulo é o 1, entao nao faz diferença se o usuario
                       #digitar ou nao o terceiro valor, pois ele já esta inicializado
    print(f'O resultado da multiplicação é de {m}')

multi(4,5)

'''
DocStrings

    Docstring é um documento da sua função, ou seja, ao se criar uma função
    a funcionalidade da mesma pode nao ficar muito clara para outros programadores
    logo voce vai criar um documento especificando o que cada parametro da sua função faz.
    
Para criar uma DocString basta colocar aspas duplas 3 vezes entre a criação da função
e o seu escopo, veja no exemplo abaixo.
'''

def subtrai(a,b):
    """

    :param a: Numero que será realizado a operação
    :param b: Numero que será realizado a operação
    :return:  Rersultado da subtração
    """
    sub = a - b
    print(f'A subtração é {sub}')


'''
Ajuda Interativa do Python

    Ao digitados help e o nome da função, o python exibe todas as informaçoes a respeito
    da função ou comando que foi especificado.
'''

help(subtrai) #aqui o python está exibindo todas as informaçoes a respeito da documentação
              #da função que criamos.

'''
Desempacotamento de funçoes:

    O desempacotamento de funçoes é usada quando nao se sabe quantos parametros
    vao ser passados pelo usuario na hora decriar a função, para informarmos ao 
    python que será usado o conceito de desempacotamento usaremos o simbolo '*' (asteristico)
    veja no exemplo abaixo.
'''

def exibir(*num): #o '*' indica que nao se sabe quantos parametros vao ser passados
    for valor in num:
        print(f'{valor}',end=' ')
    print('FIM')

exibir(4,5,7) #estou passando 3 parametros
exibir(4,0,6,9) #estou passando 4 parametros
exibir(1,2,3,4,5,6,7,8,9,10) #estou passando 10 parametros

'''
Empacotamento de Funçoes: 

    
'''

