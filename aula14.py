r = 'S'
n = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('quer continuar? [S/N] ')).upper()
    if n%2 == 0:
        print('Par')

print('Fim')