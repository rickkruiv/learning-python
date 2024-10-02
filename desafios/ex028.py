import random
from time import sleep
print('=-'*16)
print('{:^32}'.format('VAMOS JOGAR!!'))
print('=-'*16)

print('Peensando...')
sleep(2)

n = int(input('Diga-me um número de 0 a 5: '))

num = random.randint(0,5)

if n > 5:
    print('O número informado é maior que 5')
    n = int(input('Diga-me novamente um número(0 a 5): '))

elif n < 0:
    print('O número informado é menor que 0')
    n = int(input('Diga-me novamente um número(0 a 5): '))

if n == num:
    print('PARABÉNS VOCÊ ACERTOUUU!!!')
else:
    print('Que peninha, você errou :(')
    print('O número que pensei era {}'.format(num))
        
print('=-'*16)
