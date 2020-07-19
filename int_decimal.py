"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

num = float(input('Insira um numero: '))

if num == round(num):
    print('{} é um número inteiro'.format(num))
else:
    print('{} é um número decimal'.format(num))
    print('Se arrendondado para baixo: ', round(num-0.5))
    print('Se arrendondado para cima: ', round(num+0.5))
