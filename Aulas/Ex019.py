from random import randint

print('========== DESAFIO 19 ==========')

aluno1 = input('Digite nome aluno 1: ')
aluno2 = input('Digite nome aluno 2: ')
aluno3 = input('Digite nome aluno 3: ')
aluno4 = input('Digite nome aluno 4: ')

n = randint(1,4)
print('='*35)
if n ==1:
    print(f'{aluno1.upper()} foi o escolhido!')
    print('PARABENS!')
if n ==2:
    print(f'{aluno2.upper()} foi o escolhido!')
    print('PARABENS!')
if n ==3:
    print(f'{aluno3.upper()} foi o escolhido!')
    print('PARABENS!')
if n ==4:
    print(f'{aluno4.upper()} foi o escolhido!')
    print('PARABENS!')
print('='*35)




