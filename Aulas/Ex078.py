nmax = nmin = 0
num = []

for c in range(0, 5):
    num.append(int(input(f'Digite o número {c}: ')))
    if c == 0:
        nmax =  nmin = num[0]
    else:
        if num[c] > nmax:
            nmax = num[c]
        if num[c] < nmin:
            nmin = num[c]
print('{:=^55}'.format(""))
print(f'Voce digitou os numeros: {num}')
print(f'O maior valor digitado foi {nmax}, nas posição ', end='')
for i, v in enumerate(num):
    if v == nmax:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {nmin}, nas posição ', end='')
for i, v in enumerate(num):
    if v == nmin:
        print(f'{i}... ', end='')
