n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
med = (n1 + n2) / 2
print(f'\033[1;33;40m{med}\033[m')
if med < 5:
    print('\033[1;31mREPROVADO\033[m')
elif med >= 5 and med <= 6.9:
    print('\033[1;33mRECUPERAÇÂO\033[m')
elif med > 6.9 :
    print('\033[1;32mAPROVADO\033[m')