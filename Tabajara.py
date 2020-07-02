"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input('Digite o seu salário: '))

#Se o salário for menor ou igual a 280,00

if salario <= 280.00:
    por = (20/100.0)*salario
    resultado = salario + por
    print('Seu salário antes do reajuste: ',salario)
    print('Percentual aumentado: %',20)
    print('O valor do aumento é: R$: ',por)
    print('Com o reajuste o seu salário é: R$',resultado)

    #Se o salário for maior que 280,00 e menor que 700,00

elif salario > 280.00 and salario < 700.00:
    por = (15/100.0)*salario
    resultado = salario + por
    print('Seu salário antes do reajuste: ', salario)
    print('Percentual aumentado: %', 15)
    print('O valor do aumento é: R$: ', por)
    print('Com o reajuste o seu salário é: R$', resultado)

    #Se o salário for maior que 700,00 e menor que 1500,00

elif salario > 700.00 and salario < 1500.00:
    por = (10/100.0)*salario
    resultado = salario + por
    print('Seu salário antes do reajuste: ', salario)
    print('Percentual aumentado: %', 10)
    print('O valor do aumento é: R$: ', por)
    print('Com o reajuste o seu salário é: R$', resultado)

    #salários de R$ 1500,00 em diante

elif salario >= 1500.00:
    por = (5/100.0)*salario
    resultado = salario + por
    print('Seu salário antes do reajuste: ', salario)
    print('Percentual aumentado: %', 5)
    print('O valor do aumento é: R$: ', por)
    print('Com o reajuste o seu salário é: R$', resultado)