nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1 + nota2) / 2

print('A nota deste aluno é {:.1f}'.format(media))

if media < 5:
    print('O alunos está reprovado')

elif 5 <= media < 7:
    print('O aluno está de recuperação')

else:
    print('O aluno está aprovado!')