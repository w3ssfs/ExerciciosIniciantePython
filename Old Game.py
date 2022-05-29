from random import randint
tabu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
while True:
    for c in range(0, 9):
        #TABULEIRO
        print('\033[1;33m=\033[m'*30)
        for l in range(0, 3):
            for c in range(0, 3):
                print(f'\033[1;36m{tabu[l][c]:^3}\033[m', end='|')
            print()
        print('\033[1;33m=\033[m'*30)
        #JOGADA
        jogada = int(input('\033[1;33mQual sua jogada:\033[m '))
        #CPU
        cpu = randint(1 , 9)
        for l in range(0, 3):
            for c in range(0, 3):
                   if jogada == tabu[l][c]:
                       tabu[l][c] = 'X'

        for l in range(0, 3):
            for c in range(0,3):
                if cpu == tabu[l][c]:
                    tabu[l][c] = 'O'
    break

    # VENCEDOR JOGADOR





print(f'{tabu[0]}')
print(f'{tabu[1]}')
print(f'{tabu[2]}')
