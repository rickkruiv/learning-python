import random

a1 = str(input('1° Nome: '))
a2 = str(input('2° Nome: '))
a3 = str(input('3° Nome: '))
a4 = str(input('4° Nome: '))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

print('O ganhador foi {}'.format(sorteio))