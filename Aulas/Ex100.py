from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO!!')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='')
        sleep(0.2)
    print('Pronto..')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares é = {soma}')

num = list()
sorteia(num)
somaPar(num)