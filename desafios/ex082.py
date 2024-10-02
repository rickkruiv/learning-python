lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Insira um número: ')))
    r = str(input('Deseja continuar? (s/n) ')).strip()
    if r in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f'Valores da lista: {lista}')
print(f'São números pares {par}')
print(f'São números impares {impar}')
