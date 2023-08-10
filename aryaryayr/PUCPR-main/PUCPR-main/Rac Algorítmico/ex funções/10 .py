'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo
um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3
ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6,
8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

from random import randint
from time import sleep
import os

os.system('cls')
def craps(num, num2):
    soma = num + num2
    return soma

num = randint(1, 6)
num2 = randint(1, 6)
if craps(num, num2) == 7 or craps(num, num2) == 11:
    print(f'\033[1;32m{craps(num, num2)} = NATURAL - Você GANHOU!\033[m')
elif craps(num, num2) == 2 or craps(num, num2) == 3 or craps(num, num2) == 12:
    print(f'\033[1;31m{craps(num, num2)} = CRAPS - Você PERDEU!\033[m')
else:
    print(f'\033[1;33m{craps(num, num2)} = PONTO - Continue jogando.\033[m')
    sleep(1)
    c = 1
    while True:
        n3 = randint(1, 6)
        n4 = randint(1,6)
        craps(n3, n4)
        if craps(num, num2) == 7:
            print(f'{(c)}º = \033[1;31m{craps(num, num2)} - VOCÊ PERDEU\033[m')
            break
        elif craps(num, num2) == craps(n3, n4):
            print(f'{(c)}º = \033[1;32m{craps(num, num2)} - VOCÊ GANHOU\033[m')
            break
        else:
            print(f'{(c)}º = \033[1;36m{craps(n3, n4)} - continue jogando\033[m')
            sleep(1)
        c += 1
                
num1 = randint(1, 6)
num2 = randint(1, 6)
craps(num1, num2)