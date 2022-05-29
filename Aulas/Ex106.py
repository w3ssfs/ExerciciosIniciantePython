from time import sleep
c = ('\033[m',
     '\033[0;30;40m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',)

def fun(x, cor = 0):

    titulo(f"acessando o manual do comando {x}", cor=2)
    sleep(1)
    print(c[cor], end='')
    print(help(x))
    print(c[0], end='')

def titulo(msg, cor = 0):
    tam = len(msg)
    print(c[cor], end='')
    print(msg)
    print(c[0], end='')

#programa príncipal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=3)
    perg = str(input('Função ou Biblioteca: '))

    if perg.lower() == 'fim':
       break
    fun(perg, cor = 5)