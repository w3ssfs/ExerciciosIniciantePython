jogador = dict()
gols = list()
jog = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int (input(f'Quantas partidas {jogador["nome"]} Jogou: '))
for c in range(0 , partidas):
    gols.append(int(input((f'Quantos gol na partida {c}: '))))
jogador['gols'] = gols
tot = sum(gols)
jogador['total'] = tot
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O Jogador {jogador["nome"]} Jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f' => Na partida {c+ 1}°, fez {gols[c]}')
print(f'Foi um total de {tot} Gols.')
