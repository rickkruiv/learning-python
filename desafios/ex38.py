n1 = int(input('informe um número: '))
n2 = int(input('informe outro número: '))

if n1 < n2:
    maior = n2

elif n2 < n1:
    maior = n1

else:
    print('Os números são iguais')

print('{} é o maior número'.format(maior))
