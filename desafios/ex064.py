num = c = soma = 0

while num != 999:
    num += soma
    soma = num
    num = int(input('Informe um valor: '))
    c+=1
    
print('A soma dos {} números é {}'.format(c-1, soma))
