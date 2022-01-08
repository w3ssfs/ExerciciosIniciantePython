import random
print('\033[1;36m-=\033[m'*30)
print('\033[1;33m                        JOKENPÔ\033[m   ')
print('\033[1;36m-=\033[m'*30)

print('\033[1;33m                    DIGITE SEU NOME\033[m')
print('\033[1;36m-=\033[m'*30)
nome = str(input(' - ')).upper()
print('\033[1;36m-=\033[m'*30)
print(f'\033[1;33m                  BEM VINDO AO JOKENPÔ \033[m')

print('\033[1;36m-=\033[m'*30)

print('\033[1;33m                 ESCOLHA UMA DAS OPÇÕES\033[m')
print('\033[1;36m-=\033[m'*30)
print('\033[1;34m [1] PEDRA\033[m                \033[1;35m[2] PAPEL\033[m             \033[1;32m[3] TESSOURA\033[m')
print('\033[1;36m-=\033[m'*30)
luk = int(input(''))
print('\033[1;36m-=\033[m'*30)
if luk == 1:
    esc = 'pedra'.upper()
elif luk == 2:
    esc = 'papel'.upper()
elif luk ==3:
    esc = 'tessoura'.upper()
comp = random.randint(1,3)

if comp == 1:
    cpu = 'pedra'.upper()
elif comp == 2:
    cpu = 'papel'.upper()
elif comp == 3:
    cpu = 'tessoura'.upper()

print(f'       \033[1;33mVoce escolheu\033[m \033[1;32;40m{esc}\033[m \033[1;33me CPU escolheu\033[m \033[1;31;40m{cpu}\033[m')
print('\033[1;36m-=\033[m'*30)

if luk == 1 and comp == 1:
    print(' '*25+'\033[1;35;40mEMPATE\033[m')
if luk == 1 and comp ==2:
    print(' '*25+'\033[1;31;40mCPU WINS\033[m')
if luk == 1 and comp ==3:
    print(' '*25+f'\033[1;32;40m{nome} WINS\033[m')

if luk == 2 and comp == 1:
    print(' '*25+f'\033[1;32;40m{nome} WINS\033[m')
if luk == 2 and comp == 2:
    print(' '*25+'\033[1;35;40mEMPATE\033[m')
if luk == 2 and comp == 3:
    print(' '*25+'\033[1;31;40mCPU WINS\033[m')

if luk ==3 and comp ==1:
    print(' '*25+'\033[1;31;40mCPU WINS\033[m')
if luk ==3 and comp ==2:
    print(' '*25+f'\033[1;32;40m{nome} WINS\033[m')
if luk ==3 and comp ==3:
    print(' '*25+'\033[1;35;40mEMPATE\033[m')

print('\033[1;36m-=\033[m'*30)