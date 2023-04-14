pal = str(input('Insira uma palavra: '))
test = 0
h = 1
for c in pal:
    if c == pal[-h]:
        test += 1
    h += 1
if test == len(pal):
    print('A palavra {} é um palíndromo'.format(pal))
else:
    print('A palavra {} não é um palíndromo'.format(pal))

