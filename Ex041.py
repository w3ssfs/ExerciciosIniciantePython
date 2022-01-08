from datetime import date
ano = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - ano
print('SUA CATEGORIA È:')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')