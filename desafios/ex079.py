lista = []

while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado! Não foi posivel adicionar.')


    r = str(input('Deseja continuar? (S/N) ')).strip()
    if r in 'Nn':
        break
lista.sort()
print(f'esta é a sua lista {lista}')