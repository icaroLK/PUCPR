# cabeçalho
print('—'*40)
print(F'{"ORDEM CRESCENTE":^40}')
print('—'*40)
# coletando info
l = []
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}º número: '))
    l.append(num)
# result
l.sort()
print(f'Seus números em ordem crescente são:')
for i, v in enumerate(l):
    print(f'{i+1}º - {v}')