nome = str(input('Informe seu nome completo: '))
s = nome.split()
len1 = len(s[0])

print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.strip()) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(len1))

