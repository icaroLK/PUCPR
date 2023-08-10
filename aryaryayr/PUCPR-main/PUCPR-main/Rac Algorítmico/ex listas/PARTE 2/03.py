l = []
for c in range(4):
    n = int(input(f'Digite a {c+1}ª nota: '))
    l.append(n)
l.sort()
print(f'NOTAS:', end=' ')
for item in l:
    print(item, end=', ')
print()
print(f'MÉDIA: {sum(l) / len(l)}')