print('"A CALCULADORA"')
num1 = int(input('1º Numero: '))
num2 = int(input('2º Numero: '))

escolha = 0

while escolha != 5:
    print('''
    [1] somar
    [2] multiplica
    [3] maior
    [4] trocar número
    [5] sair do programa
    ''')
    escolha = int(input('Qual a sua escolha? '))

    if escolha == 1:
        print('a soma dos números é ', (num1 + num2))

    elif escolha == 2:
        print('o produto entre oa números é ', (num1*num2))

    elif escolha == 3:
        if num1 > num2:
            maior = num1

        else:
            maior = num2
        print('O maior numero é ', maior)

    elif escolha == 4:
        num1 = int(input('1º Numero: '))
        num2 = int(input('2º Numero: '))

    else:
        print('Escolha inválida')
print('FIM DO PROGRAMA')