lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    p = str(input('Quer continuar: [S/N]'))
    if p in 'nN':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.sort()
par.sort()
impar.sort()
print('='*30)
print(f'Valores digitado = {lista}')
print(f'\033[1;33mValores Pares =\033[m {par} ')
print(f'\033[1;34mValores ímpares =\033[m {impar}')