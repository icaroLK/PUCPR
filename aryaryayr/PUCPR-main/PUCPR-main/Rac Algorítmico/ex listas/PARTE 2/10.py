v1 = []
v2 = []
v3 = []
for c in range(10):
    n = int(input(f'Digite o {c+1}º valor da 1ª lista: '))
    v1.append(n)
for c in range(10):
    n2 = int(input(f'Digite o {c+1}º valor da 2ª lista: '))
    v2.append(n2)
for c in range(10):
    v3.append(v1[c])
    v3.append(v2[c])
print(f'1ª lista: {v1}')
print(f'2ª lista: {v2}')
print(f'Intercalando: {v3}')