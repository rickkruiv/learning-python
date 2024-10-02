vinte_clasificados = ('Palmeiras', 'Internacional', 'Fluminense', 
                      'Corinthians', 'Flamengo', 'Athletico-PR', 
                      'Atletico-MG', 'Fortaleza', 'São Paulo', 
                      'América-MG', 'Botafogo', 'Santos', 'Goiás', 
                      'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 
                      'Atletico-GO', 'Avaí', 'Juventude')
count = 0

for c in vinte_clasificados[:5]: 
    posicao = vinte_clasificados.index(c)+1
    print(f'{posicao}º colocado: {c}')
print('...')
for c in vinte_clasificados[-4:]:
    posicao = vinte_clasificados.index(c) +1
    print(f'{posicao}º colocado: {c}')
print(f'Times em ordem alfabetica {sorted(vinte_clasificados)}')

print('O Botafogo ficou {}º colocado'.format(vinte_clasificados.index('Botafogo')+1))
