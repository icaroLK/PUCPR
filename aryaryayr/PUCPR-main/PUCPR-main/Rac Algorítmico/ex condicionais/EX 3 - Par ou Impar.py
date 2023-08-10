from random import randint

# cabeçalho
print('—'*40)
print(f'{"Par ou Impar":^40}')
print('—'*40)

# modo de jogo
print('[1] Joagador x Máquina')
print('[2] Jogador x Jogador')
mod = int(input('Escolha o modo de jogo: '))

# jogador x máquina
if mod == 1:
    # coletando informações
    while True:
        choice = str(input('Você quer \033[1;31mPar\033[m ou \033[1;36mImpar\033[m? ')).upper()
        while True:
            num = int(input('Escolha um número de 0 a 5: '))
            if num > 5:
                print('Erro! O número deve ser inteiro e estar entre 0 a 5.')
            if num <= 5:
                break
        comp = randint(0, 5)
        sum = comp + num
        print(f'O computador escolheu \033[1;33m{comp}\033[m')
        print('~'*40)
        # calculando e mostranfo resultados
        if choice == 'PAR':
            if sum % 2 == 1:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m A soma dos números foi \033[1;35m{sum}\033[m')
            if sum % 2 == 0:
                print(f'\033[1;32mVOCÊ GANHOU!\033[m A soma dos números foi \033[1;35m{sum}\033[m')
        if choice == 'IMPAR':
            if sum % 2 == 0:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m A soma dos números foi \033[1;35m{sum}\033[m')
            if sum % 2 == 1:
                print(f'\033[1;32mVOCÊ GANHOU!\033[m A soma dos números foi \033[1;35m{sum}\033[m')
        print('~' * 40)
        print()
        resp = str(input('Deseja jogar novamente? [S/N] ')).upper()
        if resp in 'N':
            break

# jogador x jogador
if mod == 2:
    # coletando informações
    print('[1] Par')
    print('[2] Impar')
    pla1 = int(input('\033[1;33mJOGADOR 1\033[m - Par ou Impar? '))
    print('~'*40)
    if pla1 == 1:
        print('\033[1;33mJogador 1\033[m é PAR')
        print('\033[1;36mJogador 2\033[m é IMPAR')
        print('~' * 40)
        num1 = int(input('\033[1;33mJOGADOR 1\033[m - Escolha um número de 0 a 5: '))
        num2 = int(input('\033[1;36mJOGADOR 2\033[m - Escolha um número de 0 a 5: '))
        # calculando e mostranfo resultados
        sum = num1 + num2
        print('~' * 40)
        if sum % 2 == 0:
            print('\033[1;33mJOGADOR 1\033[m GANHOU!')
        else:
            print('\033[1;36mJOGADOR 2\033[m GANHOU!')

    if pla1 == 2:
        print('\033[1;33mJogador 1\033[m é IMPAR')
        print('\033[1;36mJogador 2\033[m é PAR')
        print('~' * 40)
        num1 = int(input('\033[1;33mJOGADOR 1\033[m - Escolha um número de 0 a 5: '))
        num2 = int(input('\033[1;36mJOGADOR 2\033[m - Escolha um número de 0 a 5: '))
        # calculando e mostranfo resultados
        sum = num1 + num2
        print('~' * 40)
        if sum % 2 == 0:
            print('\033[1;36mJOGADOR 2\033[m GANHOU!')
        else:
            print('\033[1;33mJOGADOR 1\033[m GANHOU!')
