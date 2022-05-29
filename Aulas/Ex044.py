print('-='*25)
print('                    LOJINHA')
print('-='*25)

print('Qual valor do Produto?')
x = float(input('R$'))
print('Qual a forma de pagamento?')
print('-='*25)
print('DINHEIRO OU CHEQUE 10% DESCONTO \nAVISTA CARTAO 5% DESCONTO \nATÉ 2X \n3X OU MAIS 20% JUROS')
print('-='*25)
print('[1] DINHEIRO/CHEQUE \n[2] CARTAO AVISTA \n[3] ATÉ 2X \n[4] 3X OU MAIS')
pag = int(input(''))
print('-='*25)
if pag == 1:
    desc = x - (x * 0.10)
    print(f'VALOR TOTAL: R${x} \nVALOR A PAGAR: R${desc} ')
elif pag == 2:
    desc = x - (x * 0.05)
    print(f'VALOR TOTAL: R${x} \nVALOR A PAGAR: R${desc} ')
elif pag == 3:
    desc = x / 2
    print(f'VALOR TOTAL: R${x} \nVALOR A PAGAR POR PARCELA: R${desc} ')
elif pag == 4:
    desc = (x * 0.20) + x
    print('QUANTAS PERCELAS (LIMITE ATÉ 10X)')
    par = int(input(''))
    pmes = desc / par
    print(f'VALOR TOTAL: R${desc} \nVALOR A PAGAR POR PARCELA: R${pmes:.2f} ')

print('-='*25)