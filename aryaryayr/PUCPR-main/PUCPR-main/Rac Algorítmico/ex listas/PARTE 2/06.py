l = []
notas_comp = []
for name in range(10):
    notas_comp.clear()
    for nota in range(4):
        n = float(input(f'{nota+1}ª nota do {name+1}º aluno: '))
        notas_comp.append(n)
        soma = sum(notas_comp)
    l.append(soma)
print('MÉDIAS:')
for c in range(10):
    print(f'{c+1} aluno: {l[c]/4:.1f}')