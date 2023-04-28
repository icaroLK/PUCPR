alt = []
ida = []

for c in range(1, 5+1):
    print(f'\n{c}° pessoa')
    ii = int(input('Idade: '))
    aa = float(input('Altura: '))
    ida.append(ii)
    alt.append(aa)

print()
alt.reverse()
ida.reverse()
print(alt)
print(ida)