import math

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: ')) 
#hip = math.sqrt((ca ** 2) + (co ** 2)) 
hip = math.hypot(co, ca)

print('A hipotenusa equivale a {:.2f}'.format(hip))