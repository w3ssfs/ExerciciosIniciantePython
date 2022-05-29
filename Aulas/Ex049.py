n = int(input('Digite um número: '))
soma = 0
print('-='*30)
for c in range(0, 11):
    soma = c * n
    print(f'              {n} x {c} = {soma}')
print('-='*30)