velo = int(input('Qual a velocidade do carro: '))
if velo > 80:
    multa = (velo - 80) * 7
if velo >80:
    print(f'Voce foi multado! Estava á {velo}Km/h na via de limite 80Km/h')
    print(f'Sua multa é de R${multa}')
else:
    print('Ésta dentro do limite, siga bem!')