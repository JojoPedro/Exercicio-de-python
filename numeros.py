n1 = float(input('Número um: '))
n2 = float(input('Número dois: '))
n3 = float(input('Número três: '))

if n1 > n2 and n1 > n3:
    print('O maior número é o: ', n1)
elif n2 > n1 and n2 > n3:
    print('O maior número é o: ', n2)
elif n3 > n1 and n3 > n2:
    print('O maior número é o: ', n3)