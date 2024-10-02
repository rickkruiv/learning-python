import math

num = int(input('informe um valor: '))
d = num*2
t = num*3
sqrt = math.sqrt(num)

print('O dobro de {} é {}, e o seu triplo é {}'.format(num, d, t))
print('A raiz quadrada de {} é {:.2f}'.format(num, sqrt))
