lanche = ['hamburger', 'suco', 'pudim', 'pizza', 'beterraba']

while True:
    lanche.append(str(input('Adicionar lanche: ')))
    
    cont = str(input('Deseja continuar? (S/N) ' )).lower().strip()
    if cont in 'n':
        break

lanche[1] = 'coca cola'
lanche.append('mouse')
lanche.insert(3, 'cachorro quente')
lanche.pop(1)
lanche.sort(reverse = True)

if 'beterraba' in lanche:
    lanche.remove('beterraba')

for c, v in enumerate(lanche):
    print(f'Na posição {c} temos {v}')

print(lanche)
print(len(lanche))
