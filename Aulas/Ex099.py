from time import sleep

def linha():
    print('-='*30)


def maior(*num):
    print('Analisando valores passados....')
    for c in num:
        sleep(0.1)
        tam = len(num)
        mai = max(num)
        print(f'{c} ', end='')
    print()
    print(f'foram informados {tam} ao todo.')
    print(f'O maior valor informado foi {mai}.')


linha()
maior(1, 2, 3, 4)
linha()
maior(4 , 63 , 2 , 11 , 6)
linha()
maior(99, 23, 42)