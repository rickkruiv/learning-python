print( '='*10,'LoJaaJ','='*10)
preço = float(input('Preço do produto: R$'))
print("""Escolha a forma de pagamento:
[ 1 ] a vista (dinheiro/cheuqe)
[ 2 ] a vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
op = int(input('Qual é a opção? '))

if op == 1:
    preço = preço * 0.90
    print('Pagando a vista em dinheiro/cheque, o valor será de R${:.2f}'.format(preço))

elif op == 2:
    preço = preço * 0.95
    print('Pagando a vista no cartão, o valor será de R${:.2f}'.format(preço))

elif op == 3:
    parcela = preço / 2
    print('O preço da parecela em 2x é de R${:.2f}, pagando no total R${:.2f}'.format(parcela, preço))

elif op == 4:
    np = int(input('Em quantas parcelas? '))
    preço = preço + (preço * 0.2)
    parcela = preço / np
    print('O valor a pagar parcelando em {}x é R${:.2f}, cada mês deve ser pago R${:.2f}'.format(np, preço, parcela))

else:
    print('Não existe está opção')
