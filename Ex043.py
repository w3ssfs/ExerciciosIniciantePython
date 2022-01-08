peso = float(input('Digite seu peso KG: '))
alt = float(input('Digite sua altura M: '))
imc = (peso / alt**2 )
print(f'SEU IMC: \033[1;33;40m{imc:.2f}\033[m')
if imc < 18.5:
    print('\033[1;34mABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[1;32mPESO IDEAL\033[m')
elif imc > 25 and imc <= 30:
    print('\033[1;36mSOBREPESO\033[m')
elif imc > 30 and imc <= 40:
    print('\033[1;37mOBESIDADE\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m')
