"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 2, 5, 10, 20, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50 e uma três notas de 2
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e duas notas de 2.
"""
print('='*30)
print('{:^30}'.format('BEM VINDO AO BANCO TABAJARA'))
print('='*30)

saque = int(input('Qual é o valor em R$ que você deseja sacar?: '))

nota = 100
total_notas = 0
while True:
    if saque >= nota:
        saque -= nota
        total_notas += 1
    else:
        if total_notas > 0:
            print(f'Total de {total_notas} notas de R${nota}')
        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        total_notas = 0
        if saque == 0:
            break
print('='*30)
print('Tenha um bom dia e volte sempre!')