aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situa'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for a, v in aluno.items():
    print(f'{a} é igual {v}')