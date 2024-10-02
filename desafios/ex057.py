sex = str(input('Qual seu sexo? [M/F]: ')).strip()[0]

while sex not in 'FMfm':
    print('Dados inválidos, insira novamente...')
    sex = str(input('Qual seu sexo? [M/F]: '))

if sex in 'Ff':
    sex = 'Feminino'
else:
    sex = 'Masculino'

print('Você é do sexo {}'.format(sex))