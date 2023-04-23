tempano = []
maior = []
maiornome = []
s = 0
nomes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for c in range(1, 12+1):
    temp = float(input('Insira a temperatuda de {} em °C: '.format(nomes[c-1])))
    s += temp
    tempano.append(temp)

m = s/12

h = 0

for c in tempano:
    if c > m:
        maior.append(c)
        maiornome.append(nomes[h])
    h += 1

tempano.append(nomes)


# print(tempano)
print('\nA média de temperatura anual foi de {:.1f}°C'.format(m))
print('Os meses que ficaram com a temperatura acima da média foram {}'.format(
    ', '.join(maiornome)))
