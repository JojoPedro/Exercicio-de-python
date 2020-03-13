"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

n1 = float(input('Insira o numero: '))
n2 = float(input('Insira o numero: '))
n3 = float(input('Insira o numero: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    lista = n1,n2,n3
elif n2 > n1 and n2 > n3 and n1 > n3:
    lista = n2,n3,n1
elif n3 > n1 and n3 > n2 and n2 > n1:
    lista = n3,n2,n1
    print('A ordem de número é: ',lista)
