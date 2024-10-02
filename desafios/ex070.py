c = tot = barato = bc = 0
print('-'*25)
print('{:^25}'.format('LOJA DO RUIVÃO'))
print('-'*25)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    bc += 1

    if bc == 1:
        baranome = nome
        barato = preco
    else:
        if preco < barato:
            baranome = nome
            barato = preco
    if preco > 1000:
        c+=1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? (S/N) '))
    if continuar in 'Nn':
        break
    
print(f'O valor total da compra é de R${tot:.2f}')
print(f'{c} produtos custão mais de R$1000.00')
print(f'{baranome} é o produto mais barato, com preço de R${barato:.2f}')