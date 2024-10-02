num = []
for c in range(0,5):
    num.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

print(f'Você digitou os seguintes valores {num}')
print(f'\nO maior valor digitado foi {maior} na posição ', end = '')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='') 

print(f'\nO menor valor digitado foi {menor} na posição ', end = '')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')