"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""

Nota1 = float(input('Digite o valor da primeira nota: '))
Nota2 = float(input('Digite o valor da segunda nota: '))

media = (Nota1 + Nota2)/2

#Nota A

if media >= 9 and media <= 10:
    print('A primeira nota é: ',Nota1)
    print('A primeira nota é: ',Nota2)
    print('-----------------------')
    print('Você tirou um A! Você foi aprovado')
    print('Sua média é de: ',media)

#Nota B

elif media >= 7.5 and media <= 9:
    print('A primeira nota é: ',Nota1)
    print('A primeira nota é: ',Nota2)
    print('-----------------------')
    print('Você tirou um B! Você foi aprovado')
    print('Sua média é de: ',media)

#Nota C

elif media >= 6 and media <= 7.5:
    print('A primeira nota é: ',Nota1)
    print('A primeira nota é: ',Nota2)
    print('-----------------------')
    print('Você tirou um C! Você foi aprovado')
    print('Sua média é de: ',media)

#Nota D

elif media >= 4 and media <= 6:
    print('A primeira nota é: ',Nota1)
    print('A primeira nota é: ',Nota2)
    print('-----------------------')
    print('Você tirou um D! Você foi reprovado')
    print('Sua média é de: ',media)

#Nota E

elif media < 4:
    print('A primeira nota é: ',Nota1)
    print('A primeira nota é: ',Nota2)
    print('-----------------------')
    print('Você tirou um E! Você foi reprovado')
    print('Sua média é de: ',media)