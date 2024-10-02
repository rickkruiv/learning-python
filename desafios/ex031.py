d = float(input('Infome a distância: '))

'''if d <= 200:
    print('Você pagara na passagem, na distância {}Km, R${:.2f}'.format(d, (0.50*d)))

else:
    print('Você pagara na passagem, na distância {}Km, R${:.2f}'.format(d, (0.45*d)))
    '''
preço = d*0.50 if d <= 200 else d*0.45

print('Você pagara na passagem, na distância {}, R${:.2f}'.format(d, preço))