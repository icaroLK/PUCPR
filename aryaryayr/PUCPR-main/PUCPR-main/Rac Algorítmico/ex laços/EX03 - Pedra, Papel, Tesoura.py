from random import randint

print('—'*40)
print(F'{"PEDRA, PAPEL, TESOURA":^40}')
print('—'*40)
l = ['Pedra', 'Papel', 'Tesoura']
p1 = []
p2 = []
win = int(input('Quantidade de pontos para vencer: '))
while True:
    print('[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura')
    choice = int(input('O que deseja jogar? '))
    comp = randint(1, 3)
    print('~' * 40)
    print(f'Você escolheu \033[1;36m{l[choice - 1]}\033[m')
    print(f'O computador escolheu \033[1;34m{l[comp - 1]}\033[m')
    if choice == 1:
        if comp == 1:
            print('\033[1;33mEMPATE\033[m')
        elif comp == 2:
            print('\033[1;31mVOCÊ PERDEU\033[m')
            p2.append(1)
        elif comp == 3:
            print('\033[1;32mVOCÊ GANHOU\033[m')
            p1.append(1)
    elif choice == 2:
        if comp == 1:
            print('\033[1;32mVOCÊ GANHOU\033[m')
            p1.append(1)
        elif comp == 2:
            print('\033[1;33mEMPATE\033[m')
        elif comp == 3:
            print('\033[1;31mVOCÊ PERDEU\033[m')
            p2.append(1)
    elif choice == 3:
        if comp == 1:
            print('\033[1;31mVOCÊ PERDEU\033[m')
            p2.append(1)
        elif comp == 2:
            print('\033[1;32mVOCÊ GANHOU\033[m')
            p1.append(1)
        elif comp == 3:
            print('\033[1;33mEMPATE\033[m')
    print('~' * 40)
    if sum(p1) == win or sum(p2) == win:
        break
print(f'PLAYER 1: {sum(p1)} pontos')
print(f'PLAYER 2: {sum(p2)} pontos')
if sum(p1) > sum(p2):
    print('Player 1 GANHOU!')
if sum(p2) > sum(p1):
    print('Player 2 GANHOU')
if sum(p1) == sum(p2):
    print('O jogo deu EMPATE')
print('~' * 40)