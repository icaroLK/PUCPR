l1 = []
l2 = []
l3 = []
pos = 0
for c1 in range(1, 3):
    for c2 in range(1, 6):
        n = int(input(f'Digite o {c2}º número da {c1}ª lista: '))
        if c1 == 1:
            l1.append(n)
        elif c1 == 2:
            l2.append(n)
for c in range(5):
    l3.append(l1[c])
    l3.append(l2[c])
print(f'Primeira lista: {l1}\n'
      f'Segunda lista: {l2}')
print(f'Intercalando: {l3}')