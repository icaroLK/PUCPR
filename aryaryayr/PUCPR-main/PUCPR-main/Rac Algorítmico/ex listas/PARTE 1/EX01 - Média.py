l = []
md = []
mu = []
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número '))
    l.append(n)
    if n >= sum(l)/6:
        mu.append(n)
    else:
        md.append(n)

print(f'Média: {sum(l)/6}\n'
      f'Notas acima da média: {mu}\n'
      f'Notas abaixo da média: {md}')