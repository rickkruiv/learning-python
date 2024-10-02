import random
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
print("""Suas opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
bot = random.randint(1, 3)
user = int(input('Qual a sua jogada? '))
print('Jogador jogou {}'.format(itens[user - 1]))
print('Computador jogou {}'.format(itens[bot - 1]))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

if bot == 1:
    if user == 1:
        print('EMPATE')
    elif user == 2:
        print('JOGADOR VENCE')
    elif user == 3:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA')

elif bot == 2:
    if user == 1:
        print('COMPUTADOR VENCE')
    elif user == 2:
        print('EMPATE')
    elif user == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA')


elif bot == 3:
    if user == 1:
        print('JOGADOR VENCE')
    elif user == 2:
        print('COMPUTADOR VENCE')
    elif user == 3:
        print('EMPATE')
    else:
        print('JOGADA')
