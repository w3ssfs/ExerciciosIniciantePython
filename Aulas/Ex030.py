# num = int(input("Digite um numero: "))
# x = num % 2
# if x == 0:
#     print(f'O número {num} é Par!')
# else:
#     print(f'O número {num} é Impar')



while True:
    num = int(input("Digite um numero: "))
    x = num % 2
    if x == 0:
        print(f'O número {num} é Par!')
    else:
        print(f'O número {num} é Impar')
    x = str(input('Quer continuar: [S/N]  ').upper())
    if x == 'N':
        break
    while x != 'S':
        print('INVALIDO')
        x = str(input('Quer continuar: [S/N]  ').upper())




