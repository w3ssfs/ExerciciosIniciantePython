c = 0
while c != 1:
    sexo = str(input('Qual seu sexo [f] ou [m]')).upper()
    if sexo == 'F':
        c += 1
        print('VOCE É FEMININA')
    elif sexo == 'M':
        c += 1
        print('VOCE É MASCULINA')
    else:
        print('INVALIDO, TENTE NOVAMENTE')

