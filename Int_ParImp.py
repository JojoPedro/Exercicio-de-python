"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""

numero = int(input('Insira um numero INTEIRO: '))
if numero % 2 == 0:
     print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))