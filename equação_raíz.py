"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math

print('digite os termos a, b, c da equação ax² + bx + c')

a = int(input('digite o termo a = '))
if a == 0:
    print('Não é uma equação do segundo grau')
else:
    b = int(input('digite o termo b = '))
    c = int(input('digite o termo c = '))
    delta = b*b - 4*a*c

    if delta < 0:
        print('A equação não possui raízes reais')
    if delta == 0:
            print('Delta =',  delta , '\nA equação possui apenas uma raiz real')

            raiz = ((-1)*b + delta/2)

            print('A raiz da equação é =', raiz)
    if delta > 0:
            print('Delta =', delta, 'A equação possui duas raizes reais')
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            print('A primeira raiz é = ', raiz1)
            print('A segunda raiz é = ', raiz2)