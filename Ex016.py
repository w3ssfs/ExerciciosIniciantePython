import math
import emoji
print('========== DESAFIO 16 ==========')

n = float(input('Digite um numero: '))
print(emoji.emojize(f'O numero {n}, tem como parte inteira {math.trunc(n)} :smile: ', use_aliases= True))

