
# alternar = True
# for oi in range(1, 8+1):
#     if alternar:
#         print("V")
#     else:
#         print("F")
#     if oi % 2 == 0:
#         alternar = not alternar


'''


def verseeh(posletra, linha):
    global alternar
    if posletra == 0:
        passo = QtdLinhas/2


    elif posletra == 1:
        passo = 2

    elif posletra == 2:
        passo = 1

    if (linha-1) % passo == 0:
        alternar = 1
        return 'V'
    else:
        alternar = 0
        return 'F'



def cu(X, linha):
    global alternar
    if X == 0:
        passo = 4

    elif X == 1:
        passo = 2

    elif X == 2:
        passo = 1
    
    if linha % passo == 0:
        return 'V'
    else:
        return 'F'
    
'''
'''
    def linhaPorLinha():
    linhao = []
    for linha in range(1, QtdLinhas+1):
        linhalist = [" "] * len(separarExpressao())


        for posletra, letra in enumerate(unicas):
            for vezcarac, carac in enumerate(separarExpressao()):
                if carac == letra:

                    linhalist[vezcarac] = VouF(posletra, linha)
                #    linhalist[vezcarac-1] = '|'
                elif carac == '|' and carac not in ('(', ')'):
                    linhalist[vezcarac] = '|'
                elif carac == '(':
                    linhalist[vezcarac] = '('
                elif carac == ')':
                    linhalist[vezcarac] = ')'
        
    #    linhao.append(''.join(linhalist))          ###TROCA AQUI PRA CONFERIR O BAGULHO
        linhao.append(linhalist)                    ###TROCA AQUI PRA CONFERIR O BAGULHO
    print(linhao)
  #  return ''.join(linhao)
'''


def bicondicional(a, b):
    if a == 'V' and b == 'V' or a == 'F' and b == 'F':
        return 'V'
    elif a == 'F' and b == 'V' or a == 'V' and b == 'F':
        return 'F'
    

print(bicondicional('F','F'))