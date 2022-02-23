count = 0
soma = 0
tt = 0
while count != 999:
    count = int(input('Numero: '))
    if count == 999:
        print('SAINDO')
    else:
        tt +=1
        soma = soma + count


print(f'Soma total = {soma:,.0f} \nValores somados = {tt}')