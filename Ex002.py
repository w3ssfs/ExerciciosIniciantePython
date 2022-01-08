cores = {
    'end': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[1;33m'
}

print(f'{cores["yellow"]}========== DESAFIO 02 =========={cores["end"]}')

nome = input(f'{cores["red"]}Digite seu nome: {cores["end"]}')
dia = input(f'{cores["red"]}Digite o Dia de seu nascimento: {cores["end"]}')
mes = input(f'{cores["red"]}Digite o Mes de seu nascimento: {cores["end"]}')
ano = input(f"{cores['red']}Digite o Ano de seu nascimento: {cores['end']}")
print('{}{}{},{} Nasceu dia:{}{}{}{}{} do mês:{}{}{}{}{} do ano:{}{}{}{}{}!{}'.format(cores['green'],nome,cores['end'], cores['yellow'],
      cores['end'],cores['green'],dia, cores['end'],cores['yellow'],cores['end'],cores['green'],mes,cores['end'],cores['yellow'],
      cores['end'],cores['green'], ano,cores['end'],cores['yellow'],cores['end']))
