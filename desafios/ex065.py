#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = c = menor = parar = soma = 0
continuar = 'S'
while continuar in 'Ss': 
    num = int(input('Digite um valor: '))
    soma += num
    c+=1    
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar != 'N' and continuar != 'S':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()    

media = soma / (c)    

print('Você digitou {} números'.format(c))
print('A soma é {} com media de {:.2f}'.format(soma, media))
print('Dos números digitados, {} é o menor e {} é o maior'.format(menor, maior))
