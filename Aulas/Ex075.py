valores = (int(input('digite um número: ' )), int(input('digite um número: ' )),
           int(input('digite um número: ' )), int(input('digite um número: ' )))

print(valores)
print(f'Quantas vezes aparece valor 9 = {valores.count(9)}')
if 3 in valores:
    print(f'Posição do Número 3 = {valores.index(3)+1}°')
else:
    print('o valor 3 não foi digitado!!!!')
print('Os valores pares foram =', end=' ')
for n in valores:
    if n % 2 ==0:
        print(f'{n}', end=' ')