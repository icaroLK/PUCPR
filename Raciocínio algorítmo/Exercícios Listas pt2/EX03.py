num = []
for c in range(1, 4+1):
    r = float(input(f'Insira a {c}° nota: '))
    num.append(r)

print('A média foi:', sum(num)/len(num))