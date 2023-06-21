def funcao_exponencial():
    def f(x, a, b):
        return a * b**x

    def grafico(a, b):
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace(-10, 10, 400)
        y = f(x, a, b)

        plt.figure(figsize=(8,6))
        plt.plot(x, y, label=f'{a}*{b}^x')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.title('Gráfico da função exponencial')
        plt.show()



    a = float(input("\033[35mInsira o valor do coeficiente a:\033[0m "))
    b = float(input("\033[35mmInsira o valor do coeficiente b:\033[0 "))

    while True:
        print("\033[33m\nEscolha uma opção:")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Gerar gráfico")
        print("4. Sair\033[0m")

        opcao = int(input("\033[33m\nOpção:\033[0m "))

        if opcao == 1:
            if b > 1:
                print("\033[32mA função é crescente.\033[0m")
            elif 0 < b < 1:
                print("\033[32mA função é decrescente\033[0m.")
            else:
                print("\033[31mOs valores inseridos para b não correspondem a uma função exponencial crescente ou decrescente.\033[0m")

        elif opcao == 2:
            x = int(input("\033[35mQual o valor de X?\033[0m"))
            print(f"\033[32mf(x) = {f(x, a, b)}\033[0m")

        elif opcao == 3:
            print(grafico(a, b))
        
        elif opcao == 4:
            break 
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")