time = list()
jogador = dict()
gols = list()
jog = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int (input(f'Quantas partidas {jogador["nome"]} Jogou: '))
    gols.clear()
    for c in range(0 , partidas):
        gols.append(int(input((f'Quantos gol na partida {c + 1}: '))))
    jogador['gols'] = gols[:]
    tot = sum(gols)
    jogador['total'] = tot
    time.append(jogador.copy())
    while True:
        resp = str(input('Adicionar Outro? [S/N] : ')).upper() [0]
        if resp in 'SN':
            break
        else:
            print('Responda S (SIM) ou N (NÃO)')
    if resp == 'N':
        break
print('=' * 40)
print('cod  ', end='')
for l in jogador.keys():
    print(f'{l:<15}', end='')
print()
print('-'* 40)
for k, v in enumerate(time):
    print(f'{k:>4} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Qual código do jogador que quer análisar? (999 para parar) : '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f' ERRO, Não existe jogador com código {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ---')
        for i, g in enumerate(time[busca] ["gols"]):
            print(f'   No jogo {i + 1} Fez {g} Gols.')
    print('-'*40)
print('<<Volte Sempre>>')