def area(lar , com):
    area = lar * com
    print(f'A área do terreno {lar:.1f} x {com:.1f} é de {area:.1f}²')

print()
print('Controle de terreno')
print('-' * 30)
l = float(input('Largura terreno: '))
c = float(input('Comprimento do terreno: '))
area(l, c)
