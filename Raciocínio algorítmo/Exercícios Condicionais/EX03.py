from random import randint
modo = resp = deu = ' '
qtde = 0

print('\033[1m{}'.format('—')*40)
print('\033[1;97m{:^56}\033[m'.format("\033[34mPAR\033[m OU \033[31mÍMPAR\033[m"))
print('\033[1m{}\033[m'.format('—')*40)

while resp not in '12':
    modo = input('\nEscolha o modo de jogo!\n'
                 '[1] Jogador x Computador\n'
                 '[2] Jogador x Jogador\nR: ')
    if modo in '12':
        break
    print('\033[31mDados inválidos.\033[m Tente novamente')

if modo in '1':
    while True:
        resp = str(input('\nVocê quer um número \033[34mpar\033[m ou \033[31mímpar\033[m? ')).strip().upper().replace('Í', 'I')[0]
        x = int(input('Insira um número: '))
        comp = randint(1, 10)
        if (x + comp) % 2 == 0:
            deu = 'P'
        elif (x + comp) % 2 != 0:
            deu = 'I'
        if resp == deu:
            print('\n\033[1;32mVOCÊ GANHOU!!!\033[m')
            print(f'\nSua escolha: {x} \nEscolha do computador: {comp} \nA soma deu:  {x+comp}')
        if resp != deu:
            print('\n\033[1;31mVOCÊ PERDEU!!!\033[m')
            print(f'\nSua escolha: {x} \nEscolha do computador: {comp} \nA soma deu:  {x+comp}')
            break
        qtde += 1
        print('\nVamos jogar novamente...')
    print(f'\nVocê obteve \033[32m{qtde}\033[m vitórias consecutivas')

elif modo in '2':

    escjog = str(input('\nJogador 1, você quer um número \033[34mpar\033[m ou \033[31mímpar\033[m? ')).strip().upper().replace('Í', 'I')[0]
    if escjog in 'P':
        print('\nJogador 1 = \033[34mPar\033[m\n'
              'Jogador 2 = \033[31mÍmpar\033[m')
    if escjog in 'I':
        print('\nJogador 1 = \033[31mÍmpar\033[m\n'
              'Jogador 2 = \033[34mPar\033[m')

    j1 = int(input('\nJogador 1: \nInsira sua jogada: '))
    j2 = int(input('Jogador 2: \nInsira sua jogada: '))

    rst = j1 + j2

    if rst % 2 == 0:
        deu = 'P'
    elif rst % 2 != 0:
        deu = 'I'

    print('\nA soma deu {}'.format(rst))
    if escjog in 'P' and rst % 2 == 0:
        print('\033[32mVencedor:\033[m Jogador 1')
    elif escjog in 'P' and rst % 2 != 0:
        print('\033[32mVencedor:\033[m Jogador 2')

    elif escjog in 'I' and rst % 2 == 0:
        print('\033[32mVencedor:\033[m Jogador 2')
    elif escjog in 'I' and rst % 2 != 0:
        print('\033[32mVencedor:\033[m Jogador 1')
