from time import sleep

print('\033[31;40m-=\033[m'*25)
print('  \033[1;33m         BEM VINDO AO FINANCIAMENTO!\033[m')
print('\033[31;40m-=\033[m'*25)
nome = str(input('\033[1;33mDigite seu nome: '))
casa = float(input('Digite valor da casa: '))
sala = float(input('Digite seu salário: '))
anos = float(input('Digite quantos anos deseja pagar: \033[m'))
mes = anos * 12
pmes = casa / mes
emp = (sala * 0.3) + sala
print('\033[1;31;40mCalculando.... \033[m')
sleep(2)
if pmes > emp:
    print('\033[1;31;40mNEGADO\033[m')
    print(f'\033[1;33mSALARIO: \033[m\033[1;32mR${sala}\033[m \n\033[1;33mPARCELA MES: \033[m\033[1;32mR${pmes:.2f}\033[m')
else:
    print('\033[1;32;40mAPROVADO\033[m')
    print(f'\033[1;33mSALARIO: \033[m\033[1;32mR${sala}\033[m \n\033[1;33mPARCELA MES: \033[m\033[1;32mR${pmes:.2f}\033[m')
