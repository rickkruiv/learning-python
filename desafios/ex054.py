from datetime import date
atual = date.today().year
dma = 0
dme = 0
for c in range(1,8):
    ano = int(input('informe a {}ºano de nascimento:'.format(c)))
    idade = atual - ano
    if idade >= 21:
        dma+=1
    else:
        dme+=1
print('{} pessoas já são de maior'.format(dma))
print('{} ainda são menores de idade'.format(dme))