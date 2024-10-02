from random import randint
import time

jogadas = 1

print('~~JOGUIN~~')
print('Pensando...')

time.sleep(2)

num = randint(0,10)
print('Pensei... Agora adivinhe!!')
print('Dica: é um número de 0 a 10...')

palpite = int(input('Que número pensei? '))

while num != palpite:
    if palpite != num:
        palpite = int(input('Você errou, tente denovo: '))

        jogadas += 1

    elif palpite == num:
        jogadas += 1
        break

print('Você acertou!!')
print('Você teve {} palpites'.format(jogadas))