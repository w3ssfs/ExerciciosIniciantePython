frase = str(input('Digite uma Frase: ')).lower()
txt = frase.replace(' ', '')
cont = frase[::-1]
txt1 = cont.replace(' ','')
print(txt)
print(txt1)
if txt == txt1:
    print('Éssa frase é palíndromo!')
else:
    print('Essa frase não é palídromo')

