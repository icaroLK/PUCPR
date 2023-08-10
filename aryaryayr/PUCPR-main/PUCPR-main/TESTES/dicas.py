""" questao numero 2 da prova """
from math import sqrt

def calc_delta(a, b, c):
    return b**2 - 4 * a * c


def calc_raiz(a, b, delta, sinal=1):
    return (-b + sinal * sqrt(delta)) / 2 * a


def baskhara(a, b, c):
    delta = calc_delta(a, b, c)
    if delta < 0:
        return None, None
    elif delta == 0:
        x = calc_raiz(a, b, delta)
        return x, None
    else:
        x1 = calc_raiz(a, b, delta)
        x2 = calc_raiz(a, b, delta, -1)
        return x1, x2


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))


tupla = baskhara(a, b, c)
if tupla[0] is None:
    print('Raizes imaginarias')
elif tupla[1] is None:
    print(f'1 raiz real: {tupla[0]}')
else:
    print(f'raiz 1 = {tupla[0]}')
    print(f'raiz 2 = {tupla[1]}')