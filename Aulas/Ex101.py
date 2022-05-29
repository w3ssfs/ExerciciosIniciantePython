def voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade < 18:
        return print(f'Com {idade} anos, VOTO NEGADO!')
    elif idade >= 18 and idade <= 65:
        return print(f'Com {idade} anos, VOTO OBRIGATÓRIO!')
    else:
        return print(f'Com {idade} anos, VOTO OPCIONAL!')


print('-'*30)
voto(int(input("Qual ano você nasceu? \n>>> ")))
