a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

maior = a
if b > a and b>c:
    maior = b
if c>a and c>b:
    maior = c

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')