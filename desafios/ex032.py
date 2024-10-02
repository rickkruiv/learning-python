from datetime import date

ano = int(input('informe um ano "0" para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 or ano % 100 == 0 or ano % 4 == 0:
    print('O ano de {} é um ano bissexto'.format(ano))

else:
    print('O ano informado({}) não é bissexto'.format(ano))