pesoM = 0
pesoN = 2000
for c in range(0, 5):
    peso = float(input('Digite seu Peso(Kg): '))
    if peso > pesoM:
        pesoM = peso
    if peso < pesoN:
        pesoN = peso
print(f'O MAIOR Peso foi {pesoM}KG e o MENOR Peso foi {pesoN}KG')