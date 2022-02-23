soma = 0
tt = 0
media = 0
maior = 0
menor = 999999999999
cont = 'S'
while cont == 'S':
    number = int(input('Número: '))
    if number > maior:
        maior = number
    if number < menor:
        menor = number
    tt +=1
    soma = soma + number
    media = soma / tt
    cont = str(input('Quer continuar: [S]/[N]').upper())
print(f'Soma Total = {soma} \nMédia = {media} \nQuantidades de Números = {tt} ')
print(f'Maior = {maior} \nMenor = {menor}')