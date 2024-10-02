dias = int(input('Qunatos dias você alugou? '))
km = float(input('Quantos quilometros você rodou?'))
#60 reais por dia e 15 centavos por km
p = (dias * 60) + (km * 0.15)
print('O valor do aluguel do carro de {} dias e {:.1f}Km rodados ficou em R${:.2f}'.format(dias, km, p))
