"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

Como é um exercicio de estrutura e decisão eu vou fazer um código usando if, elif e else... Mas poderia ser feito da
seguinte maneira

numero = int(input('Digite um número inteiro: '))
"""
numero = input('Digite um número menor que mil(1000): ')
len(numero)

if len(numero) == 3:
    print(numero[0],"centena(s),",numero[1],"dezena(s) e",numero[2],"unidade(s)")
if len(numero) == 2:
    print(numero[0],"dezena(s) e",numero[1],"unidade(s)")
if len(numero) == 1:
    print(numero[0],"unidade(s)")
else:
    if int(numero) > 1000:
        print("não sei, Rick. Me parece errado")