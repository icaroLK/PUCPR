from titulo import title
from math import sqrt
import matplotlib.pyplot as plt

def type():
    title('FUNÇÕES')
    print('[1] Afim\n'
          '[2] 2º Grau\n'
          '[3] Exponencial\n'
          '[4]   <---')


def opt_afim():
    print('[1] Raíz da função\n'
          '[2] Escolher o x\n'
          '[3] Ver gráfico\n'
          '[4]   <---')

def direcao_afim(a):
        if a > 0:
            print('A função é crescente.')
        elif a < 0:
            print('A função é decrescente.')
        else:
            print('A função é constante.')


def raiz(a, b):
    x = -b / a
    print(f'A raíz da função é {x}.')


def choose_afim(a, b, x):
    y = a*x + b
    print(f'Se x = {x}, f(x) = {y}')


def grafico_afim(x, y):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Função do 1º Grau')
    plt.show()


def vertice(a, b, c):
    xv = -b / 2*a
    yv = a*(xv**2) + b*xv + c
    print(f'Vértice: ({xv}, {yv})')
    print('Ponto mínimo.' if a > 0 else 'Ponto máximo.')


def opt_seg():
    print('[1] Raíz da função\n'
          '[2] Escolher o x\n'
          '[3] Vértices\n'
          '[4] Gráfico\n'
          '[5]   <---')


def choose_seg(a, b, c, x):
    y = a*(x**2) + b*x + c
    print(f'Se x = {x}, f(x) = {y}')


def c_delta(a, b, c):
    return b**2 - 4 * a * c

def raiz_quad(a, b, delta, sinal=1):
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
    

def grafico_seg(x, y):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Função do 2º Grau')
    plt.show()


def opt_exp(a):
    if a > 0:
        print('[1] Escolher o x\n'
            '[2] Gráfico\n'
            '[3]   <---')

    

def direcao_exp(a):
    if a > 1:
        print('A função é crescente.')
    elif 0 < a < 1:
        print('A função é decrescente.')
    elif a <= 0:
        print('A função é inexistente.')
    elif a == 1:
        print('A função é constante')

def choose_exp(a, x):
    y = a**x
    print(f'Se x = {x}, y = {y}')
    
def grafico_exp(x, y):
    plt.plot(x, y)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Função Exponencial')
    plt.show()
