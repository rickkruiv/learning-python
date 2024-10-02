pt = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))

for c in range (1, 11):
    pa = pt + (c-1)*r
    print(pa, end=", ")

print('FIM')