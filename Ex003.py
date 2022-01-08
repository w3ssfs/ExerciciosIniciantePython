print('========== DESAFIO 03 ==========')

cores = {
    'end': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[1;33m'
}

n1 = int(input(f'{cores["yellow"]}numero 1: '))
n2 = int(input(f'numero 2: {cores["end"]}'))

s = n1 + n2
s1 = bool(s == 2)
print(f'{cores["yellow"]}A soma entre{cores["end"]} {cores["red"]}{n1}{cores["end"]}'
      f'{cores["yellow"]} e {cores["end"]}{cores["red"]}{n2}{cores["end"]} {cores["yellow"]}={cores["end"]} {cores["green"]}{s}{cores["end"]}')
if s1:
    print(f'{cores["green"]}PALMEIRAS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{cores["end"]}')
