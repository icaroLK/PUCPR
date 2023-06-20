def funcoes_2():
    import matplotlib.pyplot as plt
    import numpy as np

    a = int(input('\033[35mTermo "a":\033[0m '))
    b = int(input('\033[35mTermo "b":\033[0m '))
    c = int(input('\033[35mTermo "c":\033[0m '))

    while True:
        print("\033[33m\nEscolha uma opção:")
        print("1. Calcular as raízes")
        print("2. Calcular funcão em x pedido")
        print("3. Calcular o vértice")
        print("4. Gerar gráfico")
        print("5. Sair\033[0m")

        opcao = int(input("\033[33m\nOpção:\033[0m "))

        if opcao == 1: 
            delta = b**2 + 4*a*c
            if delta > 0:
                print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes reais\033[0m')
                r1 = (-b + delta **(1/2))/ 2*a
                r2 = (-b - delta **(1/2))/ 2*a
                print(f'\033[32mAs raízes são {r1:.2f} e {r2:.2f}\033[0m')
            elif delta == 0:
                print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 1 raíz real\033[0m')
                r = -b / (2*a)
                print(f'\033[32mA raíz é {r:.2f}\033[0m')
            elif delta < 0:
                print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes complexas\033[0m')

        elif opcao == 2:
            x = int(input("\033[35mQual o valor de X?\033[0m"))
            f = (a*(x**2)+b*x+c)
            print(f'\033[32mO resultado é {f}\033[0m')
        
        elif opcao == 3:
            delta = b**2 + 4*a*c
            xv = -b / (2*a)
            yv = -(delta/(4*a))
            print(f'\033[32mO vértice da função ƒ(x)={a}x^2+{b}x+{c} é ({xv:.2f}; {yv:.2f})\033[0m ')

        elif opcao == 4:
            def f(x, a, b, c):
                return a*x**2 + b*x + c

            x = np.linspace(-10, 10, 400)
            y = f(x, a, b, c)
            plt.figure(figsize=(8,6))
            plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.legend()
            plt.title('Gráfico da função quadrática')
            plt.show()
        
        elif opcao == 5:
            break 
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")