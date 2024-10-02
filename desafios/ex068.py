import random
print('Vamos jogar!')

while True:
    botNum = random.randint(0,10)
    playerChoice = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    playerNum = int(input('Jogue um número: [0-10] '))
    soma = botNum + playerNum

    if playerChoice in 'P':
        botChoice = 'I'
    else:
        botChoice = 'P'

    if soma % 2 == 0:
        resultado = 'PAR'
        ganhador = 'P'
    else:
        resultado = 'ÍMPAR'
        ganhador = 'I'

    print(f'A soma dos números deu {soma}, no entanto é {resultado}')
    
    if playerChoice in 'P' == ganhador:
        print('PARABÉNS, VOCÊ GANHOU!!')
    elif playerChoice in 'I' == ganhador:
        print('PARABÉNS< VOCÊ GANHOU!!')
    else:
        print('VOCÊ PERDEU')
        break

print('FIM DE JOGO!')
