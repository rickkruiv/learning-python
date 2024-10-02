num = (int(input('Digite o primeiro valor: ')), 
       int(input('Digite o segundo valor: ')), 
       int(input('Digite o terceiro valor: ')), 
       int(input('Digite o ultimo valor: ')))

print(f'Você digitou os valores {num}')
print(f'O número nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número três apareceu na {num.index(3)+1}ª posição')
print('Os números pares digitados foram ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
    