from math import hypot
print('========== DESAFIO 17 ==========')

co = float(input("Digite o Cateto Oposto: "))
ca = float(input("Digite o Cateto Adjacente: "))
hip = hypot(co,ca)
print(f'CO {co} \nCA {ca} \nHIPOTENUSA {hip:.2f}')