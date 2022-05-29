sala = float(input('Qual seu salário: '))

if sala > 1250:
    sala1 = (sala * 0.10) + sala
    print(f'Seu Salário R${sala} \nNovo Salário \033[1;33mR${sala1}\033[m')
if sala <= 1250:
    sala1 = (sala * 0.15) + sala
    print(f'Seu salário R${sala} \nNovo Salário \033[1;33mR${sala1}\033[m')

