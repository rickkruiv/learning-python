n = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão
[ 1 ] coventer para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal""")
op = int(input('Sua opção: '))

if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))

else:
    print('Opção invalida')