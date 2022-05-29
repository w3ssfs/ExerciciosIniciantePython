from random import randint
from time import sleep

print('\033[1;33m-=\033[m'*40)
print('\033[34m                             JOGO DO ADVINHA 2.0\033[m')
print('\033[1;33m-=\033[m'*40)

# Sortear um número
sort = randint(1,10)
print('\033[34m                  Pensei em UM Número, Tente acertar qual!\033[m')
print('\033[1;33m-=\033[m'*40)

num_user = 0
qnt_tent = 1
#Digitar um Número
#Comparar os numeros
while num_user != sort:
    print('\033[34mConsegue Descobrir?\033[m')
    num_user = int(input('\033[1;35m>>>> \033[m'))
    print('....')
    sleep(1)

    if num_user != sort:
        qnt_tent += 1
        print('\033[1;31mErrou!\033[m')
    else:
        print('\033[1;32mParabens, Voce conseguiu!\033[m')

# Quantidades de tentativas
if qnt_tent <= 3:
    print(f'Você precisou de {qnt_tent} Para acertar, PARABENS!')
elif qnt_tent > 3 and qnt_tent <= 6:
    print(f'Voce Usou metades da sua VIDA para acertar {qnt_tent} Usadas')
elif qnt_tent > 6:
    print(f'Voce quase acabaou com suas VIDAS!!!! {qnt_tent} USADAS')