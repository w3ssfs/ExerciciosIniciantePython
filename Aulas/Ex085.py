lista = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° Valor = '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='* 40)
lista[0].sort()
lista[1].sort()
print(f'Valores Pares = {lista[0]}')
print(f'Valores Ímpares = {lista[1]}')