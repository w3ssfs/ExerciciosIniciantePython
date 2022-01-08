num = int(input('Digite um numero: '))
print('DESEJA CONVERTE')
print('[1] BINARIO \n[2] OCTAL \n[3] HEXADECIMAL')
x = int(input(''))
if x == 1:
    bi = bin(num)
    print(f'Número: {num} \nBinário: {bi}')
elif x == 2:
    he = hex(num)
    print(f'Número: {num} \nHEXA: {he}')
elif x ==3:
    oc = oct(num)
    print(f'Número: {num} \nOCTA: {oc}')
else:
    print('INVALIDO')