from random import randint
from time import sleep
print('-' * 50)
print(f'{"JOGO DA MEGA-SENA":^50}')
print('-' * 50)
jogos = int(input('Quantos Jogos: '))
tot = 0
lista = list()
game = list()
while tot <= (jogos - 1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    game.append(lista[:])
    lista.clear()
    tot +=1
print('-=' * 4 , f'Sorteando {jogos} Jogos', '-=' * 4)
for l, c in enumerate (game):
    print(f'Jogo {l+1}: {c}')
    sleep(0.5)
print('-=' * 4, 'Esses são seus RESULTADOS', '-=' * 4)