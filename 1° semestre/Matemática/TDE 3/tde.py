print('\033[35m-'*30)
print(f'{"FUNÇÕES RM":^30}')
print('-'*30)
print('\033[m')

opcao = 0
while opcao != 3:
    print()
    opcao = int(input('\033[33m[1] Função do primeiro grau\n[2] Função do segundo grau\n[3] Sair\nR:\033[m'))
    if opcao == 1:
        perg1 = 0
        while perg1 != 3:
            print()
            perg1 = int(input('\033[33m [1] Saber se a função é crescente ou decrescente\n [2] Zero da função\n [3] Voltar\nR:\033[m'))
            if perg1 == 1:
                a = int(input('Termo "a": '))
                b = int(input('Termo "b": '))
                if a > 0:
                    print(f'\033[35mA função é crescente\033[m')
                elif a < 0:
                    print(f'\033[35mA função é decrescente\033[m')
                elif a == 0:
                    print(f'\033[35mA função é reta\033[m')
            elif perg1 == 2:
                a = int(input('Termo "a": '))
                b = int(input('Termo "b": '))
                print(f'\033[35mO zero da função é {b}\033[m')
    if opcao == 2:
        perg2 = 0
        while perg2 != 3:
            print()
            perg2 = int(input('\033[33m [1] Saber as raízes\n [2] Saber o vértice \n [3] Voltar\nR:\033[m'))
            if perg2 == 1:
                    a = int(input('Termo "a": '))
                    b = int(input('Termo "d": '))
                    c = int(input('Termo "c": '))
                    delta = b**2 + 4*a*c
                    if delta > 0:
                        print(f'\033[35mA função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes reais\033[m')
                        r1 = (-b + delta **(1/2))/ 2*a
                        r2 = (-b - delta **(1/2))/ 2*a
                        print(f'\033[35mAs raízes são {r1:.2f} e {r2:.2f}\033[m')
                    elif delta == 0:
                        print(f'\033[35mA função tem 1 raíz real\033[m')
                        r = -b / (2*a)
                        print(f'\033[35mA raíz é {r:.2f}\033[m')
                    elif delta < 0:
                        print(f'\033[35mA função tem 2 raízes complexas\033[m')
            elif perg2 == 2:
                        a = int(input('Termo "a": '))
                        b = int(input('Termo "d": '))
                        c = int(input('Termo "c": '))
                        delta = b**2 + 4*a*c
                        xv = -b / (2*a)
                        yv = -(delta/(4*a))
                        print(f'\033[35mO vértice da função é ({xv:.2f}; {yv:.2f}\033[m) ')
    if opcao == 3:
        print()
        print('\033[35mObrigada volte sempre :)\033[m')