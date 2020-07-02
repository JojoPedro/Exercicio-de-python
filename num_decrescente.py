"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

n1 = int(input('Insira o numero1: '))
n2 = int(input('Insira o numero2: '))
n3 = int(input('Insira o numero3: '))

print(n1, '-', n2, '-', n3)

if (n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux

if (n2 > n1):
    aux = n2
    n2 = n1
    n1 = aux

if (n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux

print(n1, '-', n2, '-', n3)
