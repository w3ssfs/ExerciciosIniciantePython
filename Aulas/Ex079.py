num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado! Sucesso.')
    else:
        print('valor duplicado! Não adicionado.')
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'nN':
        break
print('='*30)
num.sort()
print(f'Voce Adicionou os valores: {num}')