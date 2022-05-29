from time import sleep
lista = list()
alunos = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    med = (lista[1] + lista[2]) / 2
    lista.append(med)
    alunos.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar: [S/N]'))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'{"No.":<4} {"NOME":<10}  {"MÈDIA":>8}')
print('-'*25)
for l, c in enumerate(alunos):
    print(f'{l:<4}: {c[0]:<10} {c[3]:>8}')
print("-" * 25)
while True:
    nota = int(input('Mostrar notas de qual aluno:    (999 INTERROMPE): '))
    if nota == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<' * 5, 'VOLTE SEMPRE', '>' * 5)
        break
    else:
        print(f'Notas de {alunos[nota][0]} são {alunos[nota][1:3]}')

