import random

print('========== DESAFIO 20 ==========')
#
# a1 = input('Digite o nome do aluno1: ')
# a2 = input('Digite o nome do aluno2: ')
# a3 = input('Digite o nome do aluno3: ')
# a4 = input('Digite o nome do aluno4: ')
#
# ord = [a1, a2, a3, a4]
#
# for i in (ord):
#     random.shuffle(ord)
# print(f'1° {ord[0]}  \n2° {ord[1]}  \n3° {ord[2]} \n4° {ord[3]}')


alunos = (input('Digite o nome do aluno: '), input('Digite o nome do aluno: '), input('Digite o nome do aluno: '),
          input('Digite o nome do aluno: '))
alunos = random.sample(alunos,4)
c = 1
for a in alunos:
    print(f'Foi o {c}° {a}')
    c += 1