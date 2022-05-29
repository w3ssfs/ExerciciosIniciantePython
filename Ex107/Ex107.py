from utilidadeCurso import moeda as moe
p = float(input('Digite um número:  R$ '))
au = float(input("Digite valor de aumento: "))
dis = float(input('Digite o valor de desconto: '))
print(f'A metade de {p:.2f} R$ é = {moe.metade(p):.2f} R$')
print(f'O dobro de {p:.2f} R$ é = {moe.dobro(p):.2f} R$')
print(f'Aumentando {au:.0f}% de {p:.2f} R$ é = {moe.aumento(p , au):.2f} R$')
print(f'Diminuindo {dis:.0f}% de {p:.2f} R$ é = {moe.diminuir(p, dis):.2f} R$')
