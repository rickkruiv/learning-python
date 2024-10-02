c = 0
s = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    
    if n%2 == 0:
        s+=n
        c+=1

print('São {} números pares e a soma entre eles é digitados são: {}'.format(c, s))
