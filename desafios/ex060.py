num = int(input('Informe um número: '))
c = num
factorial = 1

while c > 1:
    factorial *= c
    c -= 1

print('{}! é {}'.format(num, factorial))