num = []
O = 1

for c in range(1, 5+1):
    r = int(input(f'Digite o {c}° número: '))
    num.append(r)
    O *= r

print(f'Soma: {sum(num)}')
print(f'Multiplicação: {O}')

print('Números: ', end='')
for c in num:
    print(c, end=' / ')