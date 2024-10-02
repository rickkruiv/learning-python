dezoito = homens = mulheres = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo (F/M) ')).upper().strip()[0]
    if idade > 18:
        dezoito += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1 
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? (S/N)')).strip().upper()[0]    
    if continuar == 'N':
        break
if dezoito > 0:
    print(f'{dezoito} pessoas são maiores de dezoito')

print(f'Foram cadastradas {mulheres} mulheres menores de 20 anos')
print(f'Foram cadastrados {homens} homens')
