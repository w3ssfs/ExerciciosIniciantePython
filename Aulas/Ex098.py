from time import sleep


def contador10():
    print('Contagem de 1 em 1 até 10.')
    for c in range(1, 11, 1):
        sleep(0.1)
        print(f'{c} ', end='')
    print('fim')
    print('=' * 30)
    print('Contagem de 2 em 2 de 0 á 10.')
    for c in range(10, -2, -2):
        sleep(0.1)
        print(f'{c} ', end='')
    print('fim')
    print('=' * 30)


def contadorPerso(i, f, p):
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        if i > f:
            for c in range(i, f - p, -p):
                sleep(0.2)
                print(f'{c} ',end='')
            print('fim')
        else:
            for c in range(i, f + 1, p):
                sleep(0.2)
                print(f'{c} ', end='')
            print('fim')

contador10()
print('Agora sua vez de personalizar o contador!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passos: '))
contadorPerso(inicio, fim, passo)