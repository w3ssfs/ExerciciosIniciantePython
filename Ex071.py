print('='*30)
print('{: ^30}'.format('BANCO W3S'))
print('='*30)
valor = int(input('Quanto quer sacar: R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        totced += 1
        total -= ced
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


