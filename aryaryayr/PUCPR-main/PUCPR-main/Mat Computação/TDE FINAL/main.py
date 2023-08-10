'''
O programa deverá ser desenvolvido com a estrutura de menus aninhados (um menu
dentro do outro baseado nas opções) sendo que sempre deverá ser possível a opção de
voltar (zerando as variáveis ao recomeçar). Ainda, a persistência de dados deverá ser
utilizada, ou seja, quando ocorrer um erro de digitação ou consistência dentro do contexto,
os dados de entrada deverão ser perguntados novamente ao usuário. Dessa forma, o
programa nunca deverá ser encerrado por erro ou ao final de algum cálculo, mas sim pela
opção do usuário sair.
Deve-se utilizar funções para cada item a ser calculado, portanto, em cada chamada de
opção nos meus chame uma função
'''
from time import sleep
from os import system
from titulo import title
import conjuntos
import funcoes
import matriz
from mat import leiaFloat, leiaInt
from numpy import arange


while True:
      # opções
      system('cls')
      title('MENU')
      print('[1] Conjuntos\n'
            '[2] Funções\n'
            '[3] Matrizes\n'
            '[4] Sair')
      print('-' * 30)
      choice = leiaInt('O que deseja analisar? ')

      # operações com conjuntos
      if choice == 1:
            system('cls')

            # coletando e validando conjuntos
            a = []
            b = []
            conjuntos.valores(a, b)
            A = set(a)
            B = set(b)

            # opções
            while True:
                  system('cls')
                  print(f'Conjunto A: {A}' if len(a) != 0 else 'Conjunto A: Ø')
                  print(f'Conjunto B: {B}' if len(b) != 0 else 'Conjunto B: Ø')
                  conjuntos.opt() #opções
                  ans = leiaInt('O que deseja ver? ')
                  print('-' * 30)

                  # resultados
                  if ans == 1: #subconjunto próprio
                        conjuntos.sub_prop(A, B)
                        print('-' * 30)
                        input('<enter>')
                  elif ans == 2: #união
                        conjuntos.uniao(A, B)
                        print('-' * 30)
                        input('<enter>')
                  elif ans == 3: #intersecção
                        conjuntos.inter(A, B)
                        print('-' * 30)
                        input('<enter>')
                  elif ans == 4: #diferença
                        conjuntos.dif(A, B)
                        print('-' * 30)
                        input('<enter>')
                  elif ans == 5: #voltar
                        break
                  elif ans > 5 or ans < 1: #erro
                        print('\033[1;31mDigite uma opção válida.\033[m')
                        print('-' * 30)
                        input('<enter>')

      # funções
      elif choice == 2:
            system('cls')
            while True:
                  system('cls')
                  funcoes.type() # tipo da função
                  print('-' * 30)
                  ans = leiaInt('Escolha 1 tipo de função: ')
                  print('-' * 30)

                  # coletando coeficientes
                  if ans == 1:
                        # função afim
                        system('cls')
                        a = leiaFloat('a = ')
                        b = leiaFloat('b = ')
                        print('-' * 30)
                        while True:
                              system('cls')
                              title('FUNÇÃO AFIM')
                              print(f'f(x) = {a}x + {b}')
                              funcoes.direcao_afim(a) #crescente/decrescente
                              print('-' * 30)
                              funcoes.opt_afim() #opções
                              print('-' * 30)
                              opc = leiaInt('O que mais deseja fazer? ')
                              print('-' * 30)
                              if opc == 1: #raíz
                                    funcoes.raiz(a, b)
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 2:    #escolha o x
                                    x = leiaInt('Digite o valor de x: ')
                                    funcoes.choose_afim(a, b, x)
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 3:#gráfico
                                    x = arange(-10, 10, 0.1)
                                    y = [a*valor + b for valor in x]
                                    funcoes.grafico_afim(x, y) 
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 4: #voltar
                                    break
                              elif opc > 4 or opc < 1: #erro
                                    print('\033[1;31mDigite uma opção válida.\033[m')
                                    print('-' * 30)
                                    input('<enter>')

                  elif ans == 2:
                        # função 2º grau
                        system('cls')
                        a = leiaFloat('Digite o valor de a: ')
                        b = leiaFloat('Digite o valor de b: ')
                        c = leiaFloat('Digite o valor de c: ')
            
                        while True:
                              system('cls')
                              title('FUNÇÃO 2º GRAU')
                              print(f'f(x) = {a}x² + {b}x + {c}')
                              print('-' * 30)
                              funcoes.opt_seg() #opções
                              print('-' * 30)
                              opc = leiaInt('O que deseja fazer? ')
                              print('-' * 30)
                              if opc == 1: #raízes
                                    print(funcoes.baskhara(a, b, c))
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 2: #escolha o x
                                    x = leiaInt('Digite o valor de x: ')
                                    funcoes.choose_seg(a, b, c, x)
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 3: #vertice
                                    funcoes.vertice(a, b, c)
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 4:#gráfico
                                    x = arange(-10, 10, 0.1)
                                    y = [a*(valor**2) + b*valor + c for valor in x]
                                    funcoes.grafico_seg(x,y)
                                    print('-' * 30)
                                    input('<enter>')
                              elif opc == 5: #voltar
                                    break
                              elif opc > 5 or opc < 1: #erro
                                    print('\033[1;31mDigite uma opção válida\033[m')
                                    print('-' * 30)
                                    input('<enter>')

                  elif ans == 3:
                        # função exponencial
                        system('cls')
                        a = leiaFloat('a = ')
                        while True:
                              system('cls')
                              title('FUNÇÃO EXPONENCIAL')
                              print(f'f(x) = {a}**x')
                              funcoes.direcao_exp(a) #cresente/decrescente
                              print('-' * 30)
                              funcoes.opt_exp(a) #opções
                              if a > 0:
                                    print('-' * 30)
                                    opc = leiaInt('O que mais deseja fazer? ')
                                    print('-' * 30)
                                    
                        
                                    if opc == 1: #escolha o x
                                          x = leiaInt('Digite o valor de x: ')
                                          funcoes.choose_exp(a, x)
                                          print('-' * 30)
                                          input('<enter>')

                                    elif opc == 2: #gráfico
                                          x = arange(-10, 10, 0.1)
                                          y = [a**valor for valor in x]
                                          funcoes.grafico_exp(x, y)
                                          print('-' * 30)
                                          input('<enter>')

                                    elif opc == 3: #voltar
                                          break

                                    elif opc > 3 or opc < 1:#erro
                                          print('\033[1;31mDigite uma opção válida.\033[m')
                                          print('-' * 30)
                                          input('<enter>')
                              else:
                                    back = input('<enter>')
                                    break

                  elif ans == 4: #voltar
                        break

                  elif ans > 4 or ans < 1: # erro
                        print('\033[1;31mDigite uma opção válida\033[m')
                        print('-' * 30)
                        input('<enter>')

      # matrizes
      elif choice == 3:
            # matriz1
            system('cls')
            lin = leiaInt('Linhas: ')
            col = leiaInt('Colunas: ')
            mat = []
            matriz.prep(lin, col, mat)
            matriz.build(lin, col, mat)
            while True:
                  system('cls')
                  matriz.show(mat, lin, col, 1)
                  title('OPÇÕES')
                  matriz.opt() #opções
                  print('-' * 30)
                  opc = leiaInt('O que deseja fazer? ')
                  
                  # determinante
                  if opc == 1: 
                        print('-' * 30)
                        if matriz.valid(lin, col):
                              if lin == 2: #2x2
                                    det2 = mat[0][0]*mat[1][1] - mat[1][0]* mat[0][1]
                                    print(f'O determinante dessa matriz é {det2}')
                                    print('-' * 30)
                                    input('<enter>')
                              elif lin == 3: #3x3
                                    det3 = matriz.det(mat)
                                    print(f'O determinante dessa matriz é {det3}')
                                    print('-' * 30)
                                    input('<enter>')
                              else: # XxX 
                                    print('\033[1;34mOPS! Não consigo calcular o determinante dessa matriz!\033[m')
                                    print('-' * 30)
                                    input('<enter>')
                        else: # não quadrada
                              print('\033[1;31mERRO! A matriz não é quadrara, portanto, não é possivel calcular o determinante.\033[m')
                              print('-' * 30)
                              input('<enter>')  
                                                      
                  # multiplicar   
                  if opc == 2: 
                        #matriz2
                        system('cls')
                        lin2 = leiaInt('Linhas: ')
                        col2 = leiaInt('Colunas: ')
                        mat2 = []
                        matriz.prep(lin2, col2, mat2)
                        matriz.build(lin2, col2, mat2)
                        system('cls')
                        matriz.show(mat, lin, col, 1)
                        print(f'{"-" * 30}')
                        print(f'{"x":^30}')
                        matriz.show(mat2, lin2, col2, 2)
                        print(f'{"-" * 30}')
                        print(f'\033[1;36mMultiplicando as matrizes {lin}x{col} e {lin2}x{col2}...\033[m')
                        print(f'{"-" * 30}')
                        sleep(0.7)
                        if matriz.valid(col, lin2):
                              print(f'{"=":^30}')
                              matriz.mult(mat, mat2, lin, lin2, col2)
                        else:
                              print(f'\033[1;31mERRO! As matrizes {lin}x{col} e {lin2}x{col2} não são multiplicáveis!\033[m')
                              print(f'Para multiplicarmos uma matriz, o números de linhas da primeira matriz\ndeve ser igual ao número de colunas da segunda, ou seja, Ax\033[1mB\033[m · \033[1mB\033[mxC = AxC')
                        print('-' * 30)
                        input('<enter>')

                  # transposta
                  if opc == 3: 
                        matriz.transp(mat, col, lin)
                        print('-' * 30)
                        input('<enter>')

                  # sair      
                  if opc == 4: 
                        break
                  
                  # erro
                  elif opc > 4 or opc < 1:
                        print('\033[1;31mDigite uma opção válida\033[m')
                        print('-' * 30)
                        input('<enter>')

      # sair do programa
      elif choice == 4:
            break

      # erro
      elif choice < 1 or choice > 4:
            print('\033[1;31mDigite uma escolha válida\033[m')
            print('-' * 30)
            input('<enter>')

# fim         
print('-' * 30)
print('Obrigado pela preferência!')
print('-' * 30)