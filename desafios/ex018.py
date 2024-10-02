import math

an = int(input('Informe o ângulo: '))
a = math.radians(an)

sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)

print('Seno: {:.2f}'.format(sen))
print('Cos: {:.2f}'.format(cos))
print('tang: {:.2f}'.format(tan))