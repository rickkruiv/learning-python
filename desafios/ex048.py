soma = 0
for c in range(1, 501):
    mt = c % 3
    if mt == 0:
        soma += c
print(soma)