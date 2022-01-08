import random
from time import sleep
print("\033[1;32m-=-\033[m"*25)
print("\033[1;31m                       MiniGame do ADIVINHA")
print("\033[1;32m-=-\033[m"*25)
print('\033[37;40mVou pensar em UM número de 1 a 5.... hehe Quero ver você adivinhar!!!!!!\033[m')
print("\033[1;32m-=-\033[m"*25)
print("\033[1;33;40mPENSANDO..........\033[m")
sleep(2)
print("\033[1;32m-=-\033[m"*25)
print('\033[37;40mJá sei hahah.... Qual número eu ESCOLHI!!!! \033[m')
num = int(input('\033[1;31mQual numero você escolhe: \033[m'))
sort = random.randint(1,5)
if num == sort:
    print('\033[1;33;40mSISTEMA.....CALCULANDO.....\033[m')
    sleep(2)
    print(f'\033[1;32mVocê escolheu\033[m \033[4;33m{num}\033[m \033[1;32me COMPU Pensou no\033[m \033[4;33m{sort}\033[m')
    print('\033[1;32m PARABENS VOCÊ GANHOU! \033[m')
    print("\033[37;40mNÃOOOOO ACREDITO... VOCÊ ACERTOUUUU ... PARABÉNS !!!!!!\033[m")
else:
    print('\033[1;33;40mSISTEMA.....CALCULANDO.....\033[m')
    sleep(2)
    print(f'\033[1;32mVocê escolheu\033[m \033[4;33m{num}\033[m \033[1;32me COMPU Pensou no\033[m \033[4;33m{sort}\033[m')
    print('\033[37;40mHAHAHAHA EU VENCIIII, SOU O MELHOR HAHAHAH!\033[m')