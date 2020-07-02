"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"""
n1 = input('Primeiro num: ')
n2 = input('Segundo num: ')
n3 = input('Terceiro num: ')

    #Maior número

if n1 > n2 and n3:
    print('O maior número é o', n1)
elif n2 > n1 and n3:
    print('O maior número é o', n2)
elif n3 > n1 and n2:
    print('O maior número é o', n3)

    #Menor número

if n1 < n2 and n3:
        print('O menor número é o', n1)
elif n2 < n1 and n3:
        print('O menor número é o', n2)
elif n3 < n1 and n2:
        print('O menor número é o', n3)

