f = str(input('Escreva uma frase: ')).upper().strip()
print('Esta frase possui {} letras "A"'.format(f.count('A')))
print('O primeiro "A aparece na posiçao {}'.format(f.find('A')+1))
print('O ultimo "A" está na posição {}'.format(f.rfind('A')+1))