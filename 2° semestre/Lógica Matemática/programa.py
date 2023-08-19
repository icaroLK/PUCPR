# fazer a tabela verdade
#   →   ↔   ∧   ∨   ¬
#
#   ~((p -> q) -> ~(q -> p))
#   (p -> (q -> r))
#   ((p ^ q) -> r)
#   ((p -> (q -> r )) -> (( p -> q) -> (p -> r)))
#


expressao = input('Insira a expressão lógica: ').strip().replace('->', '→').replace('<->', '↔').replace('^', '∧').replace('v', '∨').replace('~', '¬').replace(' ','')

alf = 'abcdefghijklmnopqrstuvwxyz'
qtd = [0] * 26

print("\n\nANALISANDO: {}\n\n".format(expressao))




unicas = set()
for caracter in expressao:
    if caracter in alf:
        unicas.add(caracter)
qtd_letras = len(unicas)



### ERA AQUIOIIO

# ve quantas variáveis diferentes tem
# dicionario = {}
# ja_foi = []
# for letra in alf:
#     for pos, carac in enumerate(expressao):
#         if carac == letra and carac in ja_foi:
#             print('ja foi essa')
#             dicionario[letra].append(pos)

#         if carac == letra and carac not in ja_foi:
#             ja_foi.append(letra)
#             cu = []
#             cu.append(pos)
#             dicionario[letra] = cu
# print(dicionario)


#print(qtd)



qtd_linhas = 2**qtd_letras

print('Quantidade de linhas: {}' .format(qtd_linhas))


tab = []
for c, v in enumerate(expressao):
    tab.append(v)
    if v not in '()':
        tab.append('|')


new = ''.join(tab)











# pegar a posição de cada coisa
risco = []
disjunçao = []
conjunçao = []
bicond =[]
implic = []
negacao = []
for c, v in enumerate(new):
    if v == '|':
        risco.append(c)
    elif v == '∨':
        disjunçao.append(c)
    elif v == '∧':
        conjunçao.append(c)
    elif v == '→':
        implic.append(c)
    elif v == '↔':
        bicond.append(c)
    elif v == '¬':
        negacao.append(c)

# coloca a posiçao em que cada letra está pra depois colocar os V e F no lugar certo
dicionario = {}
ja_foi = []
for letra in alf:
    for pos, carac in enumerate(new):
        if carac == letra and carac in ja_foi:
        #    print('ja foi essa')
            dicionario[letra].append(pos)

        if carac == letra and carac not in ja_foi:
            ja_foi.append(letra)
            cu = []
            cu.append(pos)
            dicionario[letra] = cu
print(dicionario)


chaves = list(dicionario.keys())

linhao = []
pau = qtd_letras-1

tuplas = tuple(dicionario.items())
print(tuplas)

print(new)
# printa a tabela verdade arrumadinha sem os valores
for linhas in range(qtd_linhas):
    linha = []
    if linhas <= 3:
        valorlog = 'V'
    else:
        valorlog = 'F'
        
    for c, caract in enumerate(new):

        
        if c in risco:
        #    print('|', end='')
            linha.append('|')

        else:
            if caract == tuplas[pau][0]:
                linha.append(valorlog)
                

            else:
                linha.append(' ')
        #    print(' ', end='')


        
        
    
#    print('')










    buceta = ''.join(linha)
    linhao.append(buceta)
  #  linha.append('\n')

pronto = '\n'.join(linhao)
print(pronto)


#print()

for chave in dicionario.keys():
    posicoes = dicionario[chave]

    print(posicoes)

    for oi in posicoes:
        linha[oi] = 'V'
        buceta = ''.join(linha)


print('\n\n')
print(buceta)
