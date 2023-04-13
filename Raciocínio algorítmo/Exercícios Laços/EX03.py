print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("PEDRA, PAPEL OU TESOURA"))
print('\033[1m{}\033[m'.format('—')*40)

qtd = int(input('Insira a quantiade de vitória necessárias para vencer\nR: '))


v1 = v2 = 0

while True:
    print('—'*40)
    j1 = int(input('''Jogador 1:
[1] Pedra
[2] Papel
[3] Tesoura
R: '''))
    j2 = int(input('''\nJogador 2:
[1] Pedra
[2] Papel
[3] Tesoura
R: '''))
    print('—'*40)
    if j1 == j2:
        print('Empate\nNenhum jogador recebe pontos')
        print('\nPontuação atual\n1º Jogador = {} pontos\n2º Jogador = {} pontos'.format(v1, v2))

    elif j1 == 1 and j2 == 3 or j1 == 2 and j2 == 1 or j1 == 3 and j2 == 2:
        v1 += 1
        print('\nVENCEDOR DA RODADA: Jogador 1')
        print('Pontuação atual\n1º Jogador = {} pontos\n2º Jogador = {} pontos'.format(v1, v2))
        if v1 == qtd:
            print('\033[32mVENCEDOR FINAL!!!\033[m\nJogador 1 com {} pontos'.format(v1))
            break

    else:
        v2 += 1
        print('\nVENCEDOR DA RODADA: Jogador 2')
        print('\nPontuação atual\n1º Jogador = {} pontos\n2º Jogador = {} pontos'.format(v1, v2))
        if v2 == qtd:
            print('\033[32mVENCEDOR FINAL!!!\033[m\nJogador 2 com {} pontos'.format(v2))
            break



print('cabo')