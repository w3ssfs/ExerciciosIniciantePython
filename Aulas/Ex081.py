lista = []
posf = []
ff = 0
pos = 0
while True:
    n = int(input('digite um numero: '))
    lista.append(n)
    if n == 5:
        ff += 1
        posf.append(len(lista)-1)
    p = str(input('quer continuar: [S/N]'))
    if p in 'nN':
        break

cont = len(lista)
lista.sort(reverse= True)
print('='*30)
print(f'Lista contém {cont} Números digitados')
print(f'Lista na ordem Decrescente {lista}')
print(f'O número 5 aparece {ff} vezes nas posições {posf}')