num = soma = n = 0
while True:     
    num = int(input(f'Digite um valor: '))
    if num == 999:
        break
    n += 1 
    soma += num

print(f'Foram dados {n} números')
print(f'A soma de todos os números é {soma}')
