"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

numero1 = float(input('Insira o primeiro numero: '))
numero2 = float(input('Insira o segundo numero: '))
operacao = input("Qual das seguintes operações você deseja realizar? (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
    if resultado % 2 == 0:
        print('O número %d é par' % resultado)
    else:
        print('O número %d é impar' % resultado)
    if resultado >= 0:
        print('O número %d é positivo' % resultado)
    else:
        print('O número %d é negativo' % resultado)
    if round(resultado) == resultado:
        print('O número %d é inteiro' % resultado)
    else:
        print('O número %d é decimal' % resultado)

if operacao == '-':
    resultado = numero1 - numero2
    if resultado % 2 == 0:
        print('O número %d é par' % resultado)
    else:
        print('O número %d é impar' % resultado)
    if resultado >= 0:
        print('O número %d é positivo' % resultado)
    else:
        print('O número %d é negativo' % resultado)
    if round(resultado) == resultado:
        print('O número %d é inteiro' % resultado)
    else:
        print('O número %d é decimal' % resultado)

if operacao == '*':
    resultado = numero1 * numero2
    if resultado % 2 == 0:
        print('O número %d é par' % resultado)
    else:
        print('O número %d é impar' % resultado)
    if resultado >= 0:
        print('O número %d é positivo' % resultado)
    else:
        print('O número %d é negativo' % resultado)
    if round(resultado) == resultado:
        print('O número %d é inteiro' % resultado)
    else:
        print('O número %d é decimal' % resultado)

if operacao == '/':
    resultado = numero1 / numero2
    if resultado % 2 == 0:
        print('O número %d é par' % resultado)
    else:
        print('O número %d é impar' % resultado)
    if resultado >= 0:
        print('O número %d é positivo' % resultado)
    else:
        print('O número %d é negativo' % resultado)
    if round(resultado) == resultado:
        print('O número %d é inteiro' % resultado)
    else:
        print('O número %d é decimal' % resultado)