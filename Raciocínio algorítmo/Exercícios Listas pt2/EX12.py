alunos = [
    [15, 1.70],
    [16, 1.65],
    [15, 1.68],
    [14, 1.62],
    [16, 1.80],
    [15, 1.74],
    [14, 1.56],
    [16, 1.81],
    [15, 1.69],
    [14, 1.63],
    [16, 1.72],
    [15, 1.76],
    [14, 1.58],
    [16, 1.79],
    [15, 1.71],
    [14, 1.60],
    [16, 1.77],
    [15, 1.73],
    [14, 1.61],
    [16, 1.78],
    [15, 1.68],
    [14, 1.59],
    [16, 1.75],
    [15, 1.72],
    [14, 1.57],
    [16, 1.80],
    [15, 1.67],
    [14, 1.55],
    [16, 1.82],
    [15, 1.70],
]

alt = 0
qtd = 0

for oi in alunos:
    alt += oi[1]
m = alt/len(alunos)

for c in alunos:
    if c[0] >= 15:
        if c[1] < m:
            qtd += 1
print(f'Quantidade de alunos com mais de 15 anos com a altura inferior a média {m:.1f}: {qtd}')