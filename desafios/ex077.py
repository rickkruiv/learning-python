palavras = ('carro', 'bicicleta', 'moto', 'caminao', 'violao',
            'ruivo', 'liara', 'joao', 'andressa')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nNa palavra {p} temos ' , end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')