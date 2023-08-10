#-------------------------------------------------------------------------
# MATRIZ 1
matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz1[l][c] = int(input(f'Digite um valor para a posição [{l+1},{c+1}]: '))
print('-='*30)
#-------------------------------------------------------------------------
# MATRIZ 2
print()
print('Agora, digite números para a matriz 2:')

matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite um valor para a posição [{l+1},{c+1}]: '))
print('-='*30)
#-------------------------------------------------------------------------
# MATRIZES PRONTAS
print()
print('MATRIZ 1:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz1[l][c]:^5}]' , end=' ')
    print()

print()
print('MATRIZ 2:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]' , end=' ')
    print()
#-------------------------------------------------------------------------
# escolha
while True:
    print('—' * 40)
    print('[1] Soma\n'
          '[2] Subtração\n'
          '[3] Multiplicação\n'
          '[4] Divisão\n')
    resp = int(input('Que operação deseja fazer? [0 P/ PARAR] '))
    print('—' * 40)
    #-------------------------------------------------------------------------
    # SOMA
    if resp == 1:
        print('SOMA:')
        soma = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for l in range(0, 3):
            for c in range(0,3):
                soma[l][c] = matriz1[l][c] + matriz2[l][c]
        for l in range(0,3):
            for c in range(0, 3):
                print(f'[{soma[l][c]:^5}]', end=' ')
            print()

    #-------------------------------------------------------------------------
    if resp == 2:
        print('[1] Matriz 1 - Matriz 2\n'
              '[2] Matriz 2 - Matriz 1')
        sub = int(input('Escolha: '))
        if sub  == 1:
        # SUBTRAÇÃO 1
            print('SUBTRAÇÃO (M1 - M2):')
            subtr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for l in range(0, 3):
                for c in range(0, 3):
                    subtr[l][c] = matriz1[l][c] - matriz2[l][c]
            for l in range(0, 3):
                for c in range(0, 3):
                    print(f'[{subtr[l][c]:^5}]', end=' ')
                print()
        if sub == 2:
        # SUBTRAÇÃO 2
            print('SUBTRAÇÃO (M2 - M1):')
            subtr2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for l in range(0, 3):
                for c in range(0, 3):
                    subtr2[l][c] = matriz2[l][c] - matriz1[l][c]
            for l in range(0, 3):
                 for c in range(0, 3):
                    print(f'[{subtr2[l][c]:^5}]', end=' ')
                 print()

    #-------------------------------------------------------------------------
    #multiplicação
    #divisõo
    if resp > 4 or resp < 0:
        print('\033[1;31mERRO! Digite uma escolha válida.\033[m')
    if resp == 0:
        break
print(F'{" OBRIGADO! ":-^40}')