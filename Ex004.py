cores = {
    'end': '\033[m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[1;33m'
}

print(f'{cores["yellow"]}========== DESAFIO 04 ========== {cores["end"]}')

x = input(f'{cores["red"]}Digite algo: {cores["end"]}')

print(f'{cores["red"]}O tipo primitivo de {cores["end"]}{cores["green"]}{x}{cores["end"]} {cores["red"]}é{cores["end"]}',type(x))
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, está em minuscula:{cores["end"]}',x.islower())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, está em maiuscula:{cores["end"]}',x.isupper())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, é um número: {cores["end"]}',x.isnumeric())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, é letra ou número:{cores["end"]}',x.isalpha())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, é decímal:{cores["end"]}',x.isdecimal())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, tem espaço:{cores["end"]}',x.isspace())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, é um titulo:{cores["end"]}',x.istitle())
print(f'{cores["yellow"]}{x}{cores["end"]}{cores["red"]}, Nao tem espaços:{cores["end"]}',x.isalnum())