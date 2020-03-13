"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"""
n1 = float(input('Primeiro num: '))
n2 = float(input('Segundo num: '))
n3 = float(input('Terceiro num: '))

maior = n1
menor = n1

if maior < n2:
    maior = n2

if maior < n3:
    maior = n3

if menor > n2:
    menor = n2

if menor > n3:
    menor = n3

print('Maior:  ',maior)
print('Menor:  ',menor)
