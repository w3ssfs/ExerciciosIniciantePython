import datetime

pessoa = dict()
data = datetime.date.today()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    data_time =  int(input('Ano nascimento: '))
    pessoa['Idade'] =  data.year - data_time
    pessoa['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
    if pessoa['Carteira de Trabalho'] == 0:
        pessoa['Carteira de Trabalho'] = 'NULO'
        break
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário R$ '))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - data_time
    break

for k, v in pessoa.items():
    print(f'{k} tem valor {v}')