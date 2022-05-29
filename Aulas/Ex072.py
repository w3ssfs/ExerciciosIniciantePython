num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete' , 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    cont = int(input('Digite um número: '))
    if cont < 0 or cont > 20:
        print('Inválido ! Tente Novamente.', end=' ')
    else:
        print(f'Você digitou o número: {num[cont]}')
        break

