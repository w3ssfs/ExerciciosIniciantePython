from datetime import date
ano = int(input('Ano de nascimento: '))
niver = 2022
data = niver - ano

if data > 18:
    tem = data - 18
    alis = ano + 18
    print(f'quem nasceu em {ano}, tem que se alistar em {alis}.')
    print(f'Já passou {tem} ano(s) da hora de se alistar')
elif data == 18:
    print(f'Esta na hora de se alista voce tem {data} anos')
else:
    tem = 18 - data
    alis = ano + 18
    print(f'voce tem {data} anos')
    print(f'Ainda falta {tem} ano(s) para se alista')
    print(f'Seu alistamento será em {alis}')