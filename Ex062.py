n = int(input('Numero: '))
r = int(input('Razao: '))
pa = n - 1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        pa += r
        print(f'{pa}', end='')
        print(f' → ' if c < 10 else ' = ', end='')
        c += 1
    print('STOP')
    mais = int(input('Quantos a mais: '))
