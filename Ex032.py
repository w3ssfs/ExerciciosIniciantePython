import calendar
age = int(input("Qual ano você quer consultar: "))
bi = calendar.isleap(age)
if bi == True:
    print(f'o ANO {age} é BISSEXTO!')
else:
    print(f'O ANO {age} Não é bissesto!')