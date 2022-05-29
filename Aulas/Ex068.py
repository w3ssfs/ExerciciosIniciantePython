from random import randint
print('\033[36m-=\033[m'*35)
print(' \033[1;33m                     JOGO DO PAR OU IMPAR\033[m')
print('\033[36m-=\033[m'*35)
countWin = 0
life = 2
ver = 3
maisvida = 0
gameover = False
while not gameover:
    print('\033[36m-=\033[m' * 35)
    play = int(input('\033[1;33mEscolha um número: \033[m'))
    cond = str(input('\033[1;33mPar ou Ímpar > [P/I]:\033[m ').upper())
    cpu = randint(0, 20)
    print('\033[36m-=\033[m' * 35)
    resultado = cpu + play
    if resultado % 2 == 0 and cond == 'P':
        print(f'\033[1;32mVoce escolheu\033[m \033[1;34m{play}\033[m\033[1;32m '
              f'/ CPU escolheu\033[m \033[1;34m{cpu}\033[m\033[1;32m =\033[m \033[1;34m{resultado}\033[m')
        print('\033[1;32mVOCE VENCEU!..... deu PAR\033[m')
        countWin += 1
        maisvida +=1
        if maisvida == ver:
            life += 1
            maisvida = 0
            print('\033[1;32;40mVOCE GANHOU +1 VIDA!!!!!!\033[m')
        print(f'\033[1;33mVOCE TEM\033[m \033[1;32m{life}\033[m \033[1;33mVIDAS\033[m')
    elif resultado % 2 != 0 and cond == 'I':
        print(f'\033[1;32mVoce escolheu\033[m \033[1;34m{play}\033[m\033[1;32m '
              f'/ CPU escolheu\033[m \033[1;34m{cpu}\033[m\033[1;32m =\033[m \033[1;34m{resultado}\033[m')
        print('\033[1;32mVOCE VENCEU!..... deu IMPAR\033[m')
        countWin += 1
        maisvida += 1
        if maisvida == ver:
            life += 1
            maisvida = 0
            print('\033[1;32;40mVOCE GANHOU +1 VIDA!!!!!!\033[m')
        print(f'\033[1;33mVOCE TEM\033[m \033[1;32m{life}\033[m \033[1;33mVIDAS\033[m')
    elif resultado % 2 == 0 and cond == 'I':
        print(f'\033[1;32mVoce escolheu\033[m \033[1;34m{play}\033[m\033[1;32m '
              f'/ CPU escolheu\033[m \033[1;34m{cpu}\033[m\033[1;32m =\033[m \033[1;34m{resultado}\033[m')
        print('\033[1;31mVOCE PERDEU! ..... deu PAR\033[m')
        life -= 1
        maisvida = 0
        print(f'\033[1;31mVOCE TEM  {life} VIDAS!')
        if life == 0:
            print('ACABOU SUAS VIDAS GAMEOVER')
            gameover = True
    elif resultado % 2 != 0 and cond == 'P':
        print(f'\033[1;32mVoce escolheu\033[m \033[1;34m{play}\033[m\033[1;32m '
              f'/ CPU escolheu\033[m \033[1;34m{cpu}\033[m\033[1;32m =\033[m \033[1;34m{resultado}\033[m')
        print('\033[1;31mVOCE PERDEU!...... deu IMPAR\033[m')
        life -= 1
        maisvida = 0
        print(f'\033[1;31mVOCE TEM  {life} VIDAS!')
        if life == 0:
            print('ACABOU SUAS VIDAS GAMEOVER')
            gameover = True
print(f'\033[1;33mVoce Venceu\033[m \033[1;32m{countWin}\033[m \033[1;33mVezes Consecutivas\033[m')