maior = menor = 0
for c in range(1,6):
    p = float(input('Informe o {}º peso: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else: 
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))