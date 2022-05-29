from utilidadeCurso import moeda as mo


p = float(input('Digite o preço: R$ '))
au = float(input('Digite o aumento: %'))
print(f'A metade de {mo.moeda(p)} é {mo.metade(p, True)}')
print(f'O dobro de {mo.moeda(p)} é {mo.dobro(p, True)}')
print(f'Aumento de {au:.0f}% é {mo.aumento(p, au, True)}')