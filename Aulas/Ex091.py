from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 2': randint(1,6),
        'jogador 1' : randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking =  dict()
print('valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no Dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)
cont = 1
print(f'-=' *15)
print(f'{" RANKING ":=^30}')
print(f'-=' *15)

for c in ranking:
        print(f'{cont}° - {c[0]} tirou {c[1]} no Dado.')
        cont+=1