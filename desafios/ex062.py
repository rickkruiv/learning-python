pt = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da PA: '))
n = 1
total = 0
termo = 10

# pa = pt + (n - 1) * r

while termo != 0:
    total += termo
    while n <= total:
        pa = pt + (n - 1)* r
        print(pa, end = ' ')
        n+=1

    print('PAUSA...')        
    termo = int(input('Quantos termos a mais? '))
