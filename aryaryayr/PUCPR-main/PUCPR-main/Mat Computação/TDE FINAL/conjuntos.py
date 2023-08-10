from os import system
from titulo import title
from mat import leiaFloat, leiaInt

def valores(a, b):
    ca = 1
    cb = 1

    while True:
        num_a = input(f'Digite o {ca}º numero do conjunto A [" " para parar]: ')
        if num_a in '':
            break
        elif num_a.isdigit() == False:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
            continue
        a.append(int(num_a))
        ca += 1
    
    print('-'*40)
    print('CONJUNTO B')
    while True:
        num_b = input(f'Digite o {cb}º número do conjunto B [" " para parar]: ')
        if num_b in '':
            break
        elif num_b.isdigit() == False:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
            continue
        b.append(int(num_b))
        cb += 1
    print('-'*40)
    return a, b


def opt():
    title('OPÇÕES')
    print('[1] Subconjunto Próprio\n'
          '[2] União\n'
          '[3] Intersecção\n'
          '[4] Diferença\n'
          '[5]   <---')
    

def sub_prop(a, b):
    if len(a) == len(b):
        print('Nenhum dos conjuntos é subconjunto próprio do outro.')
    else:
        if a.issubset(b):
            print('A é subconjunto próprio de B.')
        elif b.issubset(a):
            print('B é um subconjunto própiro de A.')
        else:
            print('Nenhum dos conjuntos é subconjunto próprio do outro.')
        
def uniao(a, b):
    u = []
    for val in a:
        u.append(val)
    for val in b:
        u.append(val)
    U = set(u)
    print(f'A ∪ B = {U}' if len(U) != 0 else 'A ∪ B = Ø')
    

def inter(a, b):
    i = []
    for val in a:
        if val in b:
            i.append(val)
    
    I = set(i)
    print(f'A ∩ B = {I}' if len(I) != 0 else 'A ∩ B = Ø')


def dif(a, b):
    d1 = []
    d2 = []
    for val in a:
        if val not in b:
            d1.append(val)
    for val in b:
        if val not in a:
            d2.append(val)
    D1 = set(d1)
    D2 = set(d2)
    print(f'A - B = {D1}' if len(d1) != 0 else 'A - B = Ø')
    print(f'B - A = {D2}' if len(d2) != 0 else 'B - A = Ø')