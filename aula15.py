soma = num = 0
while True:
    num = int(input('Informe um número: '))

    if num == 999:
        break
    soma += num

#f string
print(f'A soma vale {soma}')

