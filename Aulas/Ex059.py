from time import sleep
c = 0
x1 = float(input('Digite um valor: '))
x2 = float(input('Digite um Valor: '))

while c != 5:
    print('-=' * 40)
    sleep(1)
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa')
    c = int(input('Qual operação realiza? '))
    print('-=' * 40)
    if c >= 6:
        print('INVALIDO!')
    if c == 1:
        soma = x1 + x2
        print(f'A soma de {x1} + {x2} = {soma}')

    if c == 2:
        soma = x1 * x2
        print(f'A multiplicação de {x1} X {x2} = {soma:.0f}')

    if c == 3:
        if x1 > x2:
            print(f'{x1} é O MAIOR')

        elif x2 > x1:
            print(f'{x2} é O MAIOR')

        else:
            print(f'{x1} e {x2} São iguais')
    if c == 4:
        x1 = float(input('Digite um valor: '))
        x2 = float(input('Digite um Valor: '))


print('End.')
