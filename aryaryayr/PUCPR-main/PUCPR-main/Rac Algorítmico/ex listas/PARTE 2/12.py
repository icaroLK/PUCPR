child = [ [12, 1.45], [13, 1.35], [14, 1.68], [11, 1.55], [13, 1.63],
          [10, 1.40], [10, 1.32], [12, 1.50], [9, 1.25], [13, 1.62],
          [10, 1.42], [9, 1.30], [14, 1.70], [11, 1.48], [13, 1.60],
          [10, 1.38], [9, 1.28], [15, 1.75], [13, 1.20], [14, 1.68],
          [12, 1.46], [13, 1.33], [13, 1.61], [10, 1.39], [14, 1.72],
          [11, 1.51], [9, 1.31], [15, 1.77], [13, 1.22], [13, 1.59] ]

h = []
a = []
for c in range(len(child)):
    h.append(child[c][1])
med = sum(h) / 30
for c in range(len(child)):
    if child[c][0] >= 13:
        if child[c][1] < med:
            a.append('.')
print(f'MÉDIA de ALTURA: {med:.2f}')
print(f'Existem {len(a)} alunos com mais de 13 anos com a altura menor que a média.')