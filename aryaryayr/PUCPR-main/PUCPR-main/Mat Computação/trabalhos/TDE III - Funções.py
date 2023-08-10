import matplotlib.pyplot as plt
from math import sqrt
from os import system

def formato(x):
    if x % 1 == 0:
        return f'{x:.0f}'
    else:
        return f'{x:.2f}'
    
def grafico(x, y):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Função do 1º Grau')
    plt.show()


def grafico_seg(x, y):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Função do 2º Grau')
    plt.show()

def primeiro(a, b):
    val = ''
    print(f'f(x) = {formato(a)}x + {formato(b)}')
    if a > 0:
        val = 'crescente'
    if a < 0:
        val = 'decrescente'
    if a == 0:
        val = 'constante'
    print(f'\033[1;36mA função é {val}!\033[m')
    print(f'Zero da função: {b*-1}/{a} = {(b*-1)/a:.2f}')

def c_delta(a, b, c):
    return b**2 - 4 * a * c

def raiz(a, b, delta, sinal=1):
    return (-b + sinal * sqrt(delta)) / 2 * a

def baskhara(a, b, c):
    delta = c_delta(a, b, c)
    if delta < 0:
        return 'Nenhuma raíz real encontrada'
    elif delta == 0:
        x = raiz(a, b, delta)
        return f'Raíz: {x}'
    else:
        x1 = raiz(a, b, delta)
        x2 = raiz(a, b, delta, -1)
        return f'Raízes: {x1} e {x2}'

def vertice(a, b, c):
    xv = -b / 2*a
    yv = a*(xv**2) + b*xv + c
    print(f'Vértice: ({xv}, {yv})')
    print('Ponto mínimo.' if a > 0 else 'Ponto máximo.')

def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;31mERRO! O usuário decidiu interromper o programa.\033[m')
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            r1 = input(num).replace(',', '.')
            r = float(r1)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número decimal.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mERRO! O usuário decidiu interromper o programa.\033[m')
            return 0
        else:
            return r
        

while True:
    system('cls')
    print('[1] Função do 1º grau\n'
          '[2] Função do 2º grau\n'
          '[3] Sair')
    print('—'*40)
    ans = leiaInt('O que deseja? ')
    if ans == 1:
        a = leiaFloat('Digite o valor de a: ')
        b = leiaFloat('Digite o valor de b: ')
        print('—'*40)
        primeiro(a, b)
        graf = str(input('Deseja gerar um gráfico? ')).strip().upper()[0]
        if graf in 'S':
            x = list(range(-10, 11))
            y = [a*valor + b for valor in x]
            grafico(x, y)

    elif ans == 2:
        a = leiaFloat('Digite o valor de a: ')
        b = leiaFloat('Digite o valor de b: ')
        c = leiaFloat('Digite o valor de c: ')
        print('—'*40)
        print(baskhara(a, b, c))
        vertice(a, b, c)
        graf = str(input('Deseja gerar um gráfico? ')).strip().upper()[0]
        if graf in 'S':
            x = list(range(-10, 11))
            y = [a*(valor**2) + b*valor + c for valor in x]
            grafico_seg(x, y)

        print('—'*40)
    elif ans == 3:
        break
    
    elif ans < 1 or ans > 3:
        print('Digite uma opção válida.')
        input('<enter>')

print('—'*40)
print('Obrigado pela preferência!')
print('—'*40)