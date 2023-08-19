# fazer a tabela verdade
#   →   ↔   ∧   ∨   ¬
#
#   ~((p -> q) -> ~(q -> p))
#   (p -> (q -> r))
#   ((p ^ q) -> r)
#   ((p -> (q -> r )) -> (( p -> q) -> (p -> r)))
#   (p ^ q)
#

def QtdLetras():
    global unicas
    unicas = set()
    for caracter in expressao:
        if caracter in alf:
            unicas.add(caracter)
    return len(unicas)


def separarExpressao():
    tab = []
    for caracter in expressao:
        tab.append(caracter)
        if caracter not in '()':
            tab.append('|')
    return ''.join(tab)



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


def caracterPosicao(x):
    for vez, carac in enumerate(separarExpressao()):
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





def verseeh(posletra, linha):



    if posletra == 0:
        return 'V' if linha <= QtdLinhas/2 else 'F'

    elif posletra == 1:
        if QtdLinhas == 8:
            return 'V' if linha not in (3, 4, 7, 8) else 'F'
        elif QtdLinhas == 4:
            return 'V' if linha % 2 != 0 else 'F'
            

    elif posletra == 2:
        return 'V' if linha % 2 != 0 else 'F'





def tudo():
    linhao = []
    for linha in range(1, QtdLinhas+1):
        linhalist = [" "] * len(separarExpressao())


        for posletra, letra in enumerate(unicas):
            for vezcarac, carac in enumerate(separarExpressao()):
                if carac == letra:

                    linhalist[vezcarac] = verseeh(posletra, linha)
                    linhalist[vezcarac-1] = '|'
        
        
        linhao.append(''.join(linhalist))
        
    return '\n'.join(linhao)


            
            
        

        










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


print('\n\n\n')


print(separarExpressao())
#print(quantoEmQuanto('q', 2))


print(tudo())