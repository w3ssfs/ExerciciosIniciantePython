num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')

    print(f'{c}', end='→ ')
if tot == 2 :
    print(f'\n \033[m O numero {num} é primo')
else:
    print(f'\n \033[mO número {num} não é primo')