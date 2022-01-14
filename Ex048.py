n = 0
soma = 0
for c in range(1, 501, 2):
    s = c%3
    if s == 0:
        n += 1
        soma += c
print(f'A soma dos {n} valores solicitados é {soma}')
