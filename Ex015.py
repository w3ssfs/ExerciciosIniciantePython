print('========== DESAFIO 15 ==========')

km = float(input('Quantos Km foram rodados: '))
dias = int(input('Quantos dias foram alugados: '))
pkm = km * 0.15
pdias = dias * 60
preco = pkm + pdias
print(f'Carro foi alugado por {dias} dias e rodou por {km} Km \nPreço por km: R${pkm}'
      f' \nPreço por Dias: R${pdias} \nPreço total: R${preco}')