add = list()
animes = list()
print('=' * 30)
print(f'{"ANIME LIST":^30}')
print('=' * 30)
print(f'{"Adicione seus animes favoritos °-°":<30}')
while True:
    add.append(str(input('Nome: ')))
    add.append(int(input('Temporadas: ')))
    add.append(int(input('Nota: ')))
    animes.append(add[:])
    add.clear()

    resp = str(input('Outro anime? [S/N]'))
    if resp in 'Nn':
        break
print('=' * 30)
print(f'{"ANIME LIST":^30}')
print('=' * 30)
print(f'{"Nome":<10} {"Temporada":^5} {"Nota":>5}')
for l, c in enumerate(animes):
    print(f'{c[0]:<20}')
print('=' * 30)
