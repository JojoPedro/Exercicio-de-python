"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

l1 = int(input('digite o tamanho do lado 1: '))
l2 = int(input('digite o tamanho do lado 2: '))
l3 = int(input('digite o tamanho do lado 3: '))
if l1 + l2 > l3:

        if l1 == l2 and l1 == l3:
            print('É um triangulo Equilátero')
        elif l1 == l2 or l2 == l3 or l1 == l3:
            print('É um triangulo Isósceles')
        elif l1 != l2 and l3 or l2 != l1 and l3 or l1 != l3:
            print('É um triangulo Escaleno')
else:
        print('Não é um triangulo')