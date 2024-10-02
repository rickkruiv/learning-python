a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
m = a*b
d = a/b
s = a+b
sb = a - b
op = a+b*b**a/a

print('A soma entre {} e {} é {}'.format(a, b, s))
print('A subtração de {} e {} é {}'.format(a, b, sb))
print('A multiplicação entre {} e {} é {}'.format(a, b, m), end=' e ')
print('{} sobre {} é {}'.format(a, b, d))

print('{}+{}*{}^{}/{} = {:.0f}'.format(a, b, b, a, a, op))