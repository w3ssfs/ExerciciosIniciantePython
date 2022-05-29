from time import sleep
#LER nome, idade, sexo 4 pessoas
somaI = 0
idadeM = 0
tnt = 0
Vnome = ''
for c in range(1, 5):
    print(f'-== {c}° Pessoa ==-')
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu Sexo [f] ou [m]: '))
    somaI += idade

    if idade > idadeM and sexo == 'm':
        Vnome = nome
        idadeM = idade
    if sexo == 'f' and idade < 20:
        tnt +=1
med = somaI / 4
print('\033[31m ANALISANDO\033[m')
sleep(3)

print(f'A média de idade no grupo é {med} Anos')
print(f'O {Vnome} é o Homem mais velho')
print(f'Tem {tnt} Mulheresa menores de 20 anos')


