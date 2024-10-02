casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos vai pagar? '))

prestação = casa / (anos * 12)
minimo = sal * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos'.format(sal, anos), end='')
print(' a prestação de R${:.2f}'.format(prestação))

if prestação <= minimo:
    print('Emprestimo concedido')

else:
    print('Emprestimo negado')