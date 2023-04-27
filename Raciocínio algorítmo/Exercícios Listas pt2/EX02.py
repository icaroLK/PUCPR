num = []
for c in range(1, 10+1):
    r = float(input(f'Insira o {c}° número: '))
    num.append(r)


num.reverse()
for c in num:
    print(c, end=' / ')