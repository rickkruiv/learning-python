from random import randint
import time

jogadas = 0

print('~~JOGUIN~~')
print('Pensando...')

time.sleep(2)

num = randint(0,10)
print('Pensei... Agora adivinhe!!')
print('Dica: é um número de 0 a 10...')

acertou = False

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    jogadas += 1
    if palpite == num:
        acertou = True

print('Você acertou!!')
print('Você teve {} palpites'.format(jogadas))