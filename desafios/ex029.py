v = float(input('Qual a velocidade do veiculo? '))

if v > 80:
    print('Este veiculo está acima do limite, ele será multado.')
    print('Sua multa é de R${:.2f}'.format(7*(v-80)))
else:
    print('Boa, amigão!! Continue assim.')