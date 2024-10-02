from datetime import date
nascimento = int(input('Informe o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    categoria = 'Mirim'
elif idade <=14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('O atleta tem {} e sua categoria é {}'.format(idade, categoria))