"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e
a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
"""

valor_hora = float(input('Digite o valor da sua hora de trabalho: '))
quant_hora_trabalhada = int(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = (valor_hora*quant_hora_trabalhada)

fgts = (salario_bruto*11)/100
sindi = (salario_bruto*3)/100.0

#Salário Bruto até 900

if salario_bruto <= 900.00:
    salario_liquido = salario_bruto - sindi

#Salário Bruto até 1500 (inclusive) - desconto de 5%

elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = (salario_bruto*5)/100.0
    salario_liquido = salario_bruto - ir - sindi

#Salário Bruto até 2500 (inclusive) - desconto de 10%

elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = (salario_bruto*10)/100
    salario_bruto = salario_bruto - ir - sindi

#Salário Bruto acima de 2500 - desconto de 20%

else:
    ir = (salario_bruto*20)/100
    salario_liquido = salario_bruto - ir - sindi

print('Seu salario bruto é de: R$ %7.2f' % salario_bruto)
print('O valor do FGTS é: %7.2f' % fgts)
print('O desonto do sindicato é de: %7.2f' %sindi)
print('Seu salario liquido é de: R$ %7.2f' % salario_liquido)