while True:
    n = int(input('Informe um valor: '))
    if n < 0:
        break
    print('-'*25)
    for m in range(1,11):
        print(f'{m} x {n} = {m*n}')
    print('-'*25)
print('PROGRAMA FINALIZADO')
