n = int(input('Digite um número: '))
s = 0
print('\033[33m (!) Divisivel \033[34m (!) Não divisivel')
for c in range(1, n+1):
    if n%c == 0:
        print('\033[33m', end='')
        s += 1
    else: 
        print('\033[34m', end='')
    print(c, end=' ')
print('\n\033[mO número {} é dividido por {} números '.format(n, s))
if s == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')