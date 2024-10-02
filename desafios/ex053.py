frase = str(input('Escerva uma frase: ')).upper()
f = frase.replace(' ', '')

if f == f[::-1]:
    print('A frase "{}" é palindromo'.format(frase))
else: 
    print('A frase "{}"não é um palindromo'.format(frase))