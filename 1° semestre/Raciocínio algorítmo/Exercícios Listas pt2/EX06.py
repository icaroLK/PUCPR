alunos = []


for c in range(1,5+1):
    print(f'\n{c}° aluno')
    notas = []
    for alu in range(1, 4+1):
        n = float(input(f'Nota {alu}: '))
        notas.append(n)
    print(f'Média: {sum(notas)/len(notas)}')
    alunos.append(notas)


print('\nALUNOS APROVADOS\n')
for c, i in enumerate(alunos):
    if (sum(i)/len(i)) >= 7:
        print(f'Aluno {c+1} com {sum(i)/len(i)} de média')
