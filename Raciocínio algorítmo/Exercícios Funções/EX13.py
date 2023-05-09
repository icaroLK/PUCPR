def mold(linha, coluna):
    for lin in range(1, linha):
        if lin == 1 or lin == linha-1:
            for borda in range(1, coluna+1):
                if borda == 1 or borda == coluna:
                    print('+', end='')
                else:
                    print('{}'.format('\033[1;97m––\033[m'), end='')
            print()
        
        vazio = '  ' * (coluna-2)
        if lin == linha-1:
            break
        print('{0}{1}{0}'.format('|', vazio))
        
    


while True: 
    linha = input('Insira a quantidade de linhas: ')
    try:
        qtdlin = int(linha)
        if qtdlin < 1 or qtdlin > 20:
            print('Insira um valor entre 1 e 20')
        else:
            break
    except:
        print('Insira um número')

while True: 
    coluna = input('Insira a quantidade de colunas: ')
    try:
        qtdcolu = int(coluna)
        if qtdcolu < 1 or qtdcolu > 20:
            print('Insira um valor entre 1 e 20')
        else:
            break
    except:
        print('Insira um número')

mold(qtdlin, qtdcolu)