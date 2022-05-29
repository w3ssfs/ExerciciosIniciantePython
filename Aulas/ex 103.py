def ficha(nome="<desconhecido>", gol=0):
    print(f'O jogador {nome}, fez {gol} gol(s) no campeonato!')


#PROGRAMA PRINCIPAL
jnome = input('Nome do jogador: ')
ngol = input('Números de gol(s): ')
if ngol.isnumeric():
    n = int(ngol)
else:
    ngol = 0
if jnome.strip() == '':
    ficha(gol=ngol)
else:
    ficha(jnome, ngol)