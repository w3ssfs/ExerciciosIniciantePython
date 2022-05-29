print('-='*40)
print('                                  TABUADA')
print('-='*40)
c = 0
while c >= 0:
    c = int(input('Qual número deseja ver a tabúada: '))
    if c >= 0:
        for v in range(0,11):
            tabu = v * c
            print(f'{c} x {v} = {tabu}')
print('Tabuada encerrada!')