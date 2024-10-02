peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / ((altura / 100) **2)

if 18.5 <= imc < 25:
    res = 'NORMAL'
elif 25 <= imc < 30:
    res = 'SOBREPESO'
elif 30 <= imc < 40:
    res = 'OBESIDADE'
elif 40 <= imc:
    res = 'OBESIDADE GRAVE'

print('Seu índice de massa coporal é {:.1f} ({})'.format(imc, res))
