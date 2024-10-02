si = 0
med = 0
maioridadeh = 0
nomevelho = ''
mulher20 = 0
for p in range(1, 5):
    print('_----{}ª pessoa----_'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    si += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20+=1
med = si / 4
print('A média de idade do grupo é de {:.0f} anos'.format(med))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, maioridadeh))
print('São {} mulhere(s) menor(es) de 20 anos'.format(mulher20))