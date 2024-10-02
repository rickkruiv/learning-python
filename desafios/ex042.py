print('-='*20)
print('Analizador de Triângulo')
print('-='*20)
r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        tr = 'equilatero'
    elif r1 != r2 != r3 != r1: 
        tr = 'escaleno'
    else:
        tr = 'isóceles'
        
    print('Os segmentos acima podem formar um triânfulo {}'.format(tr))
else:
    print('Os segmentos acima não podem formar triângulos')
