lis1 = []
lis2 = []
tudo = []
oi = pu = 0


for c in range(1, 2+1):
    for g in range(1, 5+1):
        elem = input('Insira o {}° elemento da {}° lista: '.format(g, c))
        if c == 1:
            lis1.append(elem)
        elif c == 2:
            lis2.append(elem)

for c in range(len(lis1) + len(lis2)): #dava pra ter colocado só 10 ja q temos os termos predefinidos
    if c % 2 == 0:
        tudo.append(lis1[oi])
        oi += 1
    elif c % 2 != 0:
        tudo.append(lis2[pu])
        pu += 1


print('\n1° Lista:', lis1)
print('2° Lista:', lis2)
print('Lista intercalada:', tudo)
print()