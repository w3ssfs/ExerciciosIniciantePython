from time import sleep
import emoji
r = 5
print('\033[1;33mFALTA 10 SEGUNDOS PARA OS FOGOS DE ARTIFICIOS\033[m')
for c in range(10, 0, -1):
    if c == 5:
        for x in range(c,0, -1):
            r = -2
            print(f'\033[1;33mFALTAM EXATOS\033[m \033[1;31m{x} SEGUNDOS\033[m')
            sleep(1)
    if c <= 10 and r >= 5:
        print(f'\033[1;33mFALTAM EXATOS\033[m \033[1;32m{c} SEGUNDOS\033[m')
        sleep(1)
print(emoji.emojize('BUMMMMMMMM :thumbs_up:'))