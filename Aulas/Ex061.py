n = int(input('Numero: '))
r = int(input('Razao: '))
pa = n - 1
c = 1
while c <= 10:
    pa += r
    print(f'{pa}', end='')
    print(f' → ' if c < 10 else ' = ', end='')
    c += 1
print('DONE')
