pt = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))
n = 1

# pa = pt + (n - 1) * r

while n <= 10:
    pa = pt + (n - 1)* r
    print(pa, end = ' ')
    n+=1
    