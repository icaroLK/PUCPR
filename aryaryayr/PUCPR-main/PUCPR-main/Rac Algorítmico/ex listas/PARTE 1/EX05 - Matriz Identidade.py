tam = int(input('Digite a largura da matriz: '))
matriz = [[0] * tam for c in range(tam)]
for c in range(0, tam):
    matriz[c][c] = 1


for l in range(0, tam):
    print('|', end='')
    for c in range(0, tam):
        print(f'{matriz[l][c]:^5}', end='')
    print('|')
