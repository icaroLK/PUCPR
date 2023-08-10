def contorno(linha=1, coluna=1):
    if linha > 20:
        linha = 20
    if coluna > 20:
        coluna = 20
    for c in range(coluna):
        if c == 0:
            print(f'{"+"}{"–" * (linha-1)}{"+"}')
        elif coluna-1 > c > 0:
            print(f'|', ' ' * (linha-3), f'|')
        elif c == coluna-1:
            print(f'{"+"}{"–" * (linha-1)}{"+"}')
    print()

print()
contorno(10,20)