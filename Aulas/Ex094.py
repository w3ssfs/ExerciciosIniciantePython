grupo = list()
pessoa =  dict()
tot = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo = [F/M]: ').upper())
    pessoa['Idade'] = int(input('Idade: '))
    if pessoa['Idade'] > 0 :
        tot += pessoa['Idade']
    if pessoa['Sexo'] == 'F':
        pessoa['Mulheres'] = pessoa['Nome']
    grupo.append(pessoa.copy())

    cont = str(input('Quer continuar? [S/N] :'))
    if cont in 'Nn':
        break
cont_pessoa = len(grupo)
media = tot / cont_pessoa
print('-='*30)
print(f'- O grupo contém {cont_pessoa} Pessoas.')
print(f'- A média de idade é {media:.2f} anos.')
print(f'- As mulheres cadastradas foram {pessoa["Mulheres"]}')