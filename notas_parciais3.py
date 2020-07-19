"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota1 = float(input('insira a primeira nota: '))
nota2 = float(input('insira a segunda nota: '))
nota3 = float(input('insira a terceira nota: '))

media = (nota1 + nota2 + nota3)/2

if media >= 7 and media < 10:
    print('a primeira nota é', nota1)
    print('a segunda nota é', nota2)
    print('a terceira nota é', nota3)
    print('Você foi aprovado')

elif media < 7:
    print('a primeira nota é', nota1)
    print('a segunda nota é', nota2)
    print('a terceira nota é', nota3)
    print('Infelizmente você foi reprovado!')

elif media >=10:
    print('Parabéns! Você foi aprovado com distincção')

else:
    print('Notas invalidas')