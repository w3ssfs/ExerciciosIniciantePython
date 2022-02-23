print('{:-^40}'.format(""))
print('{: ^40}'.format('LOJÃO DO BARATÃO'))
print('{:-^40}'.format(""))
barato = ''
total = totmil = cont = menorp =  0
while True:
    produto = str(input('nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menorp:
        menorp = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]').strip().upper()[0])
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total é R$ {total:,.2f}')
print(f'Tem {totmil} produtos custando mais de R$ 1,000,00 ')
print(f'O produto mais barato foi {barato}custando R$ {menorp:,.2f}')

