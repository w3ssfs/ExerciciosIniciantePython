
fim = False
qntIdade = 0
qntSexo = 0
qntMulher = 0
while not fim:
    print('='*30)
    print('     CADASTRO DE PESSOAS')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ').upper())
    print('=' * 30)

    if idade >= 18:
        qntIdade += 1
    if sexo == 'M':
        qntSexo +=1
    if idade < 20 and sexo == 'F':
        qntMulher +=1

    ver = str(input('Quer continuar? [S/N]').upper())
    if ver == 'N':
        fim = True
print(f'Tem {qntIdade} +18 \nTem {qntSexo} Homens cadastrado \nTem {qntMulher} mulheres menores de 20 anos ')