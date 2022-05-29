print('========== DESAFIO 12 ==========')

preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
print(f'Preço: R${preco} \ndesconto de 5% = R${desconto:.2f} \nValor com desconto: R${preco - desconto:.2f}')