v1 = []
v2 = []
v3 = []
v4 = []
for c in range(10):
    n = int(input(f'Digite o {c+1}º valor da 1ª lista: '))
    v1.append(n)
for c in range(10):
    n2 = int(input(f'Digite o {c+1}º valor da 2ª lista: '))
    v2.append(n2)
for c in range(10):
    n3 = int(input(f'Digite o {c+1}º valor da 3ª lista: '))
    v3.append(n3)
for c in range(10):
    v4.append(v1[c])
    v4.append(v2[c])
    v4.append(v3[c])
print(f'1ª lista: {v1}')
print(f'2ª lista: {v2}')
print(f'3ª lista: {v3}')
print(f'Intercalando: {v4}')