print('=========== DESAFIO 01 ===========')

cores = {
    'clean': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
}

nome = input(f'{cores["amarelo"]}Qual seu nome: {cores["clean"]}')

print(f'{cores["amarelo"]}Olá{cores["clean"]} {cores["verde"]}{nome}{cores["clean"]} {cores["amarelo"]}! Prazer em te conhecer!{cores["clean"]}')
