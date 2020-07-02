"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dia = input('Digite 1-Segunda 2-Terça 3-Quarta 4-Quinta 5-Sexta 6-Sábado 7-Domingo: ')

if dia == '1':
    print('Segunda-feira')
elif dia == '2':
    print('Terça-feira')
elif dia == '3':
    print('Quarta-feira')
elif dia == '4':
    print('Quinta-feira')
elif dia == '5':
    print('Sexta-feira')
elif dia == '6':
    print('Sábado')
elif dia == '7':
    print('Domingo')
else:
    print('Entrada invalida')