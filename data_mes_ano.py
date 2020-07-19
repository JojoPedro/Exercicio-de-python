"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

validade = False

# MESES COM 31 DIAS
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
        mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        validade = True

    # MESES COM 30 DIAS
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        validade = True
    elif mes == 2:

    # TESTA SE O ANO É BISSEXTO
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if (dia <= 29):
                validade = True
    elif (dia <= 28):
        validade = True

if (validade):
    print("data válida")
else:
    print("data inválida")
