a = int(input("Primerio valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if (a + b < c) or (b + c < a) or (c + a < b):
    print('Não é um triângulo')
elif (a==b) and (a==c):
    print('triângulo equilatero')
elif (a==b) or (c==a) or (b==c):
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')
