from math import factorial

c = int(input('Numero: '))
n = c
if n < 0:
    print('INVALIDO')
else:
    while n > 0:
        print(f'{n}', end='')
        print(f' x ' if n > 1 else ' = ', end='')
        n -=1
    print(f'{factorial(c)}', end='')