soma = 0
ct = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        soma += c
        ct += 1
print(soma, ct)