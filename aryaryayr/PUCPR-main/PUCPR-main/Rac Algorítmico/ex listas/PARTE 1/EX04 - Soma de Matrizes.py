matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz1[l][c] = int(input(f'Digite o número para a posição \033[1;36m({l+1},{c+1}): \033[m'))

matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite o númeor para a posição \033[1;33m({l+1},{c+1}): \033[m'))

print('\033[1;36mMATRIZ 1:\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz1[l][c]:^5}]', end=' ')
    print()
print(f'{"+":^24}')
print('\033[1;33mMATRIZ 2:\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]', end=' ')
    print()
print(f'{"=":^24}')
print('\033[1;32mMATRIZ 3\033[m')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz1[l][c] + matriz2[l][c]:^5}]', end=' ')
    print()
