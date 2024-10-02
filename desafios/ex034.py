sal = float(input('Informe seu salário: R$'))

if sal > 1250.00:
    a = 10
    sal = sal + (sal*0.1)

else:
    a = 15
    sal = sal + (sal*0.15)

print('Seu aumento será de {}%, no entanto, você receberá R${:.2f}'.format(a, sal))