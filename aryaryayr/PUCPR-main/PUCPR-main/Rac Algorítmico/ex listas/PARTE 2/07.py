l = [2, 65, 343, 1, 9]
print(l)
print(f'SOMA: {sum(l)}')
print(f'MULTIPLICAÇÃO: ', end='')
res = 1
for v in l:
    res *= v
print(res)
