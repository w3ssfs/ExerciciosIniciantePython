from datetime import date
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento: '))
    data = date.today().year - ano
    if data >=  18:
        maior += 1
    else:
        menor += 1
print(f'tem {maior} Pessoas de maioridade e {menor} Pessoas de menor idade')