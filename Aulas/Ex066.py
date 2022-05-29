count = 0
soma = 0
c = 0
while count != 999:
    count = int(input('Digite um valor (999 para parar!)'))
    if count != 999:
        c += 1
        soma = soma + count
print(f'Digitou {c} Números, Soma de {soma:,.0f}')

