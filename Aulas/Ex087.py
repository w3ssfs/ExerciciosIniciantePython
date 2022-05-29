matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = ter = t = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
        if matriz[l][2] != -0:
            ter += matriz[l][c]
        for c in matriz[1]:
            if c > t:
                t = c
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'A soma dos valores pares são {s}')
print(f'A soma dos valores da terceira coluna são {ter}')
print(f'O maior número da segunda fila é {t}')