from math import factorial as fac
def fatorial(num, show = False):
    """
    -->> Calcula o fatorial de um Número.
    :param num: Número a ser calculado.
    :param show: True para mostra cálculos, False para Ocultar cálculos.
    :return: Retorna Valor do Fatória.
    """
    if show == True:
        for n in range(num, 0, -1):
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

    return fac(num)

print(fatorial(int(input('Digite um numero: ')), ))

