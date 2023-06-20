def matrizes():
    def criar_matriz(linhas, colunas):
        return [[int(input(f'\033[35mInforme o elemento [{i+1},{j+1}]: \033[0m')) for j in range(colunas)] for i in range(linhas)]

    def imprimir_matriz(matriz):
        print('\033[32m[')
        for linha in matriz:
            print('  ', linha)
        print(']\033[0m')

    def determinante(matriz):
        if len(matriz) == len(matriz[0]) == 2:
            return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        elif len(matriz) == len(matriz[0]) == 3:
            return matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1] - matriz[0][2]*matriz[1][1]*matriz[2][0] - matriz[0][1]*matriz[1][0]*matriz[2][2] - matriz[0][0]*matriz[1][2]*matriz[2][1]
        else:
            return None

    def multiplicacao(matriz1, matriz2):
        if len(matriz1[0]) != len(matriz2):
            return None

        resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

        for i in range(len(matriz1)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]

        return resultado

    def transposta(matriz):
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


    linhas = int(input('\033[35mInforme o número de linhas:\033[0m '))
    colunas = int(input('\033[35mInforme o número de colunas:\033[0m '))
    matriz1 = criar_matriz(linhas, colunas)

    print('\033[32mMatriz de entrada:\033[0m')
    imprimir_matriz(matriz1)

    while True:
        print("\033[33m\nEscolha uma opção:")
        print("1. Determinante (se a matriz for 2x2 ou 3x3)")
        print("2. Multiplicação")
        print("3. Matriz Transposta")
        print("4. Sair\033[0m")

        opcao = int(input("\033[33m\nOpção:\033[0m "))
        
        if opcao == 1:
            print('\033[32mDeterminante (se a matriz for 2x2 ou 3x3):\033[0m')
            det = determinante(matriz1)
            if det is not None:
                print(det)
            else:
                print('\033[31mA matriz não é quadrada ou não é de ordem 2 ou 3.\033[0m')

        elif opcao == 2:
            linhas = int(input('\033[35mInforme o número de linhas da segunda matriz:\033[0m '))
            colunas = int(input('\033[35mInforme o número de colunas da segunda matriz:\033[0m '))
            matriz2 = criar_matriz(linhas, colunas)

            mult = multiplicacao(matriz1, matriz2)
            if mult is not None:
                print('\033[32mA x B =\033[0m')
                imprimir_matriz(mult)
            else:
                print('\033[31mA multiplicação entre as matrizes não é possível.\033[0m')

        elif opcao == 3:
            print('\033[32mMatriz transposta:\033[0m')
            imprimir_matriz(transposta(matriz1))
        
        elif opcao == 4:
            break 
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")