par = []
imp = []

for c in range(1, 20+1):
    n = int(input(f'Insira o {c}° número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)

print('\nLista de pares: ')
for c in par:
    print(c, end=' / ')

print('\n\nLista de ímpares: ')
for c in imp:
    print(c, end=' / ')