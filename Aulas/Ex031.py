dis = int(input("Qual a DISTANCIA da viagem em KM: "))
if dis <= 200:
    valor = 0.50 * dis
    print(f'O valor da PASSAGEM é R${valor}')
else:
    valor = 0.45 * dis
    print(f'O valor da PASSAGEM é R${valor}')