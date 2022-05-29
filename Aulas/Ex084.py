pessoas = list()
dados = list()
mai = men = 0
while True:
    #leitura dos Dados
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Quer Continuar: [S/N]'))
    if cont in 'Nn':
        break

print(f'{len(pessoas)} Pessoas Cadastradas!')
print(f'Maior peso {mai} Kg, Peso de ',end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end=', ' if )
print()
print(f'Menor peso {men} Kg, Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ', end=', ')