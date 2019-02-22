print('\033[1;33m-\033[m'*100)
print('{:>70}'.format('\033[1;30mPYTHON THE BEST LANGUAGE\033[m'))# o ':>' é para alinhar o texto a direita
print('\033[1;33m-\033[m'*100)

print('\n')

while True:
    escolha = int(input('''\033[1;30mEscolha uma opção:\033[m 

                        \033[1;34mQuem criou a Linguagem Python?                 [1]\033[m 
                        \033[1;32mO que é a linguagem Python?                    [2]\033[m
                        \033[1;36mDiferencial da linguagem Python                [3]\033[m
                        \033[1;31mPor que aprender em Python?                    [4]\033[m
                        \033[1;33mRelação do python com a cobra piton            [5]\033[m
                        \033[1;35mPor que o logo é representado por duas cobras? [6]\033[m
                                                                            '''))

    print('\n')

    if escolha == 1:
        print('''\033[1;30m     A linguagem foi criada pelo Holandês Guido van Rossum em 1991, teve a
    inspiração do nome em um programa de televisão britanico 'Monty Python’s Flying Circus\033[m\n''')

    elif escolha == 2:
        print('''\033[1;30m     Python é uma linguagem de programação de alto nível, interpretada
    orientada a objetos e funcional com principal foco em produtividade e legibilidade\033[m\n''')

    elif escolha == 3:
        print('''\033[1;30m     A syntaxe da linguagem Python é muito simples em relação as outras linguagens,alem de ser 
    multiplataforma,ou seja,é executavel em diferentes tipos de sistemas operacionais.\033[m\n''')

    elif escolha == 4:
        print('''\033[1;30m     Python é uma linguagem que vem ganhando muito espaços nos ambientes
   corporativos, muito usada em inteligencia artificial, um ramo que vem crescendo bastante
   nos ultimos anos, e pelo simples fato de ser \033[1;34mMUITOOOOO DIVERTIDO\033[m \033[1;30mprogramar em python\n''')

    elif escolha == 5:
        print('''\033[1;30m     Por anos Guidor evitou vincular a linguagem ao réptil (a cobra píton), porem
    editora O’Reilly — que possui a tradição de utilizar animais nas capas de seus livros 
    sugeriu colocar uma cobra píton na capa do seu p4rimeiro livro "Programming Python"\033[m\n''')

    elif escolha == 6:
        print('''\033[1;30m     Uma das teorias é que o simbolo da linguagem, quando desfocado,é na verdade
    as iniciais 'Py' de Python\033[m\n''')

    else:
        break