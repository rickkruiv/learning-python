numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
                   'cinco', 'seis', 'sete', 'oito', 'nove',
                   'dez', 'onze', 'doze', 'treze', 'quatorze', 
                   'quinze', 'dezeseis', 'dezesete', 'dezoito', 
                   'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número (0-20): '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente', end='')

print(f'Você escolheu o número {numeros_extenso[numero]}')
