# fazer a tabela verdade
#   →   ↔   ∧   ∨   ¬
#
#   ~((p -> q) -> ~(q -> p))
#   (p -> (q -> r))
#   ((p ^ q) -> r)
#   ((p -> (q -> r )) -> (( p -> q) -> (p -> r)))

#   ((p|→|(q|→|r|))→|((p|→|q|)→|(p|→|r|)))

#   (p ^ q)
#

def QtdLetras():
    global unicas
    unicas = set()
    for caracter in expressao:
        if caracter in alf:
            unicas.add(caracter)
    return len(unicas)


def separarExpressao(a=0):
    tab = []
    for caracter in expressao:
        tab.append(caracter)
        if caracter not in '()':
            tab.append('|')
    if a == 0:
        return ''.join(tab)
    elif a == 1:
        return tab



def posCarac(x):
    lista = []
    for vez, carac in enumerate(separarExpressao()): # aqui ele vai achar a posicao na expressao ja separada
        if carac == str(x):
            lista.append(vez)
       #     return vez
    if len(lista) == 0:
        print('Caracter não encontrado')
    else:
        return lista


def caracterPosicao(x, frase):
    for vez, carac in enumerate(frase):
        if vez == x:
            return carac



def colocarXnoY(x, y):
    linha = []
    for vez, carac in enumerate(separarExpressao()):
        
        if carac == y:

            linha.pop()
            linha.append('|')
            linha.append(x)
        else:
            linha.append(' ')
#    return ''.join(linha)
    return linha #trabalhando com isso vai ficar melhor la na frente



def quantoEmQuanto(Y, passo):
    linhas = []
    alternar = True
    for linha in range(1, QtdLinhas+1):
        if alternar:
            #print(colocarXnoY('V', Y))
            linhas.append(colocarXnoY('V', Y))
        else:
           # print(colocarXnoY('F', Y))
            linhas.append(colocarXnoY('F', Y))
        if linha % passo == 0:
            alternar = not alternar
#    return '\n'.join(linhas)
    return linhas



def implicacao(a, b):
    if a == 'V' and b == 'V' or a == 'F' and b == 'V' or a == 'F' and b == 'F':
        return 'V'
    elif a == 'V' and b == 'F':
        return 'F'

def disjuncao(a, b):
    if a == 'V' and b == 'V' or a == 'F' and b == 'V' or a == 'V' and b == 'F':
        return 'V'
    elif a == 'F' and b == 'F':
        return 'F'
    
def conjuncao(a, b):
    if a == 'V' and b == 'V':
        return 'V'
    elif a == 'F' and b == 'F' or a == 'F' and b == 'V' or a == 'V' and b == 'F':
        return 'F'
    
def bicondicional(a, b):
    if a == 'V' and b == 'V' or a == 'F' and b == 'F':
        return 'V'
    elif a == 'F' and b == 'V' or a == 'V' and b == 'F':
        return 'F'
    






def VouF(posletra, linha):



    if posletra == 0:
        return 'V' if linha <= QtdLinhas/2 else 'F'

    elif posletra == 1:
        if QtdLinhas == 8:
            return 'V' if linha not in (3, 4, 7, 8) else 'F'
        elif QtdLinhas == 4:
            return 'V' if linha % 2 != 0 else 'F'
            

    elif posletra == 2:
        return 'V' if linha % 2 != 0 else 'F'



#   ((p -> (q -> r )) -> (( p -> q) -> (p -> r)))

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
        
        #  →   ↔   ∧   ∨   ¬

        linhaarrumada = ''.join(linhalist)
        for vezcarac, carac in enumerate(linhaarrumada):
            jafoi = set()
            for cu in range(1):
                if vezcarac == confParent()[cu]:
                    jafoi.add(confParent()[cu])

                    if separarExpressao()[vezcarac+3] == '→':
                        resp = implicacao(caracterPosicao(confParent()[cu]+1, linhaarrumada), caracterPosicao(confParent()[cu]+5, linhaarrumada))
                    elif separarExpressao()[vezcarac+3] == '↔':
                        resp = bicondicional(caracterPosicao(confParent()[cu]+1, linhaarrumada), caracterPosicao(confParent()[cu]+5, linhaarrumada))
                    elif separarExpressao()[vezcarac+3] == '∧':
                        resp = conjuncao(caracterPosicao(confParent()[cu]+1, linhaarrumada), caracterPosicao(confParent()[cu]+5, linhaarrumada))
                    elif separarExpressao()[vezcarac+3] == '∨':
                        resp = disjuncao(caracterPosicao(confParent()[cu]+1, linhaarrumada), caracterPosicao(confParent()[cu]+5, linhaarrumada))

                    linhalist[vezcarac+3] = resp

        6 7 8 10 11 12
        menor = separarExpressao(1)
        menor.pop()



        linhao.append(''.join(linhalist))          ###TROCA AQUI PRA CONFERIR O BAGULHO
    #    linhao.append(linhalist)                    ###TROCA AQUI PRA CONFERIR O BAGULHO
  #  print(linhao)
    return '\n'.join(linhao)






            
def confParent():
    nicole = False
    posi = []

    for vez, carac in enumerate(separarExpressao()):
        if carac == '(':
            if nicole == True:
                nicole = False
                posi = []
            else:
                nicole = True
                posi.append(vez)
        if carac == ')' and nicole == True:
            posi.append(vez)
            break
    return posi




        










# Variáveis
alf = 'abcdefghijklmnopqrstuvwxyz'
qtd = [0] * 26






expressao = input('Insira a expressão lógica: ').strip().replace('->', '→').replace('<->', '↔').replace('^', '∧').replace('v', '∨').replace('~', '¬').replace(' ','')
print("\n\nANALISANDO: {}\n\n".format(expressao))

QtdLinhas = 2**QtdLetras()


print('Quantidade de letras: {}' .format(QtdLetras()))
print('Quantidade de linhas: {}' .format(QtdLinhas))
print(f'Frase separada: {separarExpressao()}\n\n\n')

#print(posCarac('q'))
#print(caracterPosicao(3))


# print('\n\n')
# for vez in posCarac('∧'):
#     print(caracterPosicao(vez-2))
#     print(caracterPosicao(vez))
#     print(caracterPosicao(vez+2))
# print('\n\n')





print(separarExpressao())
#print(quantoEmQuanto('q', 2))


print(linhaPorLinha())

print('\n\n\n')

#print(confParent((separarExpressao())))


confParent()