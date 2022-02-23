times = ('América-MG', 'Palmeiras','Athletico-PR', 'Athletico-GO', 'Athletico-MG', 'Avai',
         'Botafogo', 'Bragantino', 'ceará', 'Corinthians', 'Coritiba'
         ,'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goias',
         'Internacional', 'Juventos',  'Santos', 'São paulo')

while True:
    print('\033[33mLista de Times Brasileirão\033[m')
    print(times)
    print('\033[;33mOs 5 Primeiros\033[m')
    print(f'{times[0:5]}')
    print('\033[;33mOs últimos 4\033[m')
    print(f'{times[-4:]}')
    print('\033[33mOrdem Alfabetica\033[m')
    print(f'{sorted(times)}')
    print('\033[33mQual posição esta o Palmeiras\033[m')
    print(f'Palmeiras está na posição = {times.index("Palmeiras")+1}°')
    break
