print('{:-^40}'.format('-'))
print('{:^40}'.format('LISTAGEM DE PREÇO'))
print('{:-^40}'.format('-'))

loja = ('Lápiz', 1.75, 'borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
        'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'livros', 34.90)
for pos in range(0, len(loja)):
    if pos % 2 == 0:
        print(f'{loja[pos]:.<30}', end='')
    else:
        print(f'R$ {loja[pos]:>7,.2f}')
print('{:-^40}'.format('-'))
