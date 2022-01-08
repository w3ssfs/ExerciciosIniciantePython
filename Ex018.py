import math
print('========== DESAFIO 18 ==========')

ang = float(input('Digite um ãngulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Ângulo {ang:.0f}° \nCosseno {cos:.2f} \nSeno {sen:.2f} \nTangente {tan:.2f}')
