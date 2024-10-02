#fibonacci = soma do ultimo termo com o novo ex: (5 , 8, 13)

termos = int(input('Quantos termos mostrar? '))
t1 = 0
t2 = 1
c = 0

print('{} - {}'.format(t1,t2), end = ' - ')
while termos >= c:
    t3 = t1 + t2
    print('{}'.format(t3), end = ' - ')
    t1 = t2
    t2 = t3
    c+=1

print('FIM')