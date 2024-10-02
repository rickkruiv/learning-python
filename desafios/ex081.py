lista = []
while True:
    lista.append(int(input('Informe um número: ')))
    r = str(input('Deseja continuar? (s/n)')).strip().lower()
    if r == 'n':
        break

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')

if 5 in lista:
    pos = lista.index(5)
    print(f'O núero cinco foi digitado e está na posição {pos+1}')
else:
    print('O número cinco não foi encotrado na lista0')

