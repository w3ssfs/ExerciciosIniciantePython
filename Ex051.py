ini = int(input('Inicio: '))
ra = int(input('Razão: '))
fim = ini + (11-1) * ra
for c in range(ini, fim, ra):
    print(f'{c} ', end='→ ')
print('Acabou')