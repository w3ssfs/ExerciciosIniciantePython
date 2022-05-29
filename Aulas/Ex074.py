from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Números sorteados:')
maior = menor = 0
for c in num:
     print(f'{c} ', end= '')
print(f'\nMaior Número: {max(num)}')
print(f'Menor Número: {min(num)}')

