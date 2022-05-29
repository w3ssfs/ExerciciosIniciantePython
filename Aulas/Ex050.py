soma = 0
con = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    par = n%2
    if par == 0:
        con += 1
        soma += n
print(f'Total {con} Valores PARES \nSoma {soma}')