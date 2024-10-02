from datetime import date

nascimento = int(input('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade < 18:
    print('Você ainda vai se alistar daqui {} anos ({})'.format((18 - idade), ano + (18- idade)))

elif idade > 18:
    print('Você já devia ter se alistado faz {} anos ({})'.format((idade - 18), ano - (idade - 18)))

else:
    print('Já está na hora de se alistar, soldado!!')