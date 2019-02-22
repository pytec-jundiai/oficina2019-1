# Importando módulo criado
import calculadora

valor1 = input('Digite o valor 1: \n')

valor2 = input('Digite o valor 2: \n')


# Usando função do módulo da calculadora
res = calculadora.somar(valor1, valor2)


print('Reposta é: {}'.format(res))
