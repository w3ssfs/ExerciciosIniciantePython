def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;31mERRO !, Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor

#programa principal
n = leiaint('Digite um número: ')
print(f'Número digítado foi {n}')