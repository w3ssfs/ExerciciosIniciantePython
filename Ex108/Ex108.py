from utilidadeCurso import moeda as mo


p = float(input('Digite o preço: R$ '))
au = float(input('Digite o aumento: %'))
print(f'A metade de {mo.moeda(p)} é {mo.moeda(mo.metade(p))}')
print(f'O dobro de {mo.moeda(p)} é {mo.moeda(mo.dobro(p))}')
print(f'Aumento de {au:.0f}% é {mo.moeda(mo.aumento(p, au))}')