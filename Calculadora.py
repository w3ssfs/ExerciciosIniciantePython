import math
print('\033[33m-='*35)
print('                          Calculadora\033[m')
print('\033[33m-=\033[m'*35)

i = 1
while i == 1:
    num = float(input('number: '))
    num2 = float(input('number two: '))
    print('[1] Dividir \n[2] Multiplicar \n[3] Somar \n[4] Subtrair \n[5] Raiz \n[6] Quadrado')
    ope = int(input(':'))
    if ope == 1:
        tot = num / num2
        print(f'{num} / {num2} = {tot:.2f}')
    elif ope == 2:
        tot = num * num2
        print(f'{num} * {num2} = {tot:.2f}')
    elif ope == 3:
        tot = num + num2
        print(f'{num} + {num2} = {tot}')
    elif ope == 4:
        tot = num - num2
        print(f'{num} - {num2} = {tot:.2f}')
    elif ope == 5:
        tot = math.sqrt(num)
        print(f'{tot}')
    elif ope == 6:
        tot = math.pow(num,num2)
        print(f'{tot}')
    else:
        print('fora de contexto')
    cont = int(input('\033[1;32mDeseja continuar\033[m [1] sim [2] não \n:'))
    if cont != 1:
        i = 0
        print('fim')



