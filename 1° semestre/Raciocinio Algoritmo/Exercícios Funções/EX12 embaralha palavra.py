from random import choice


def embaralhe(normal):
    pera = [0] * len(normal)


    cu = []
    for c in range(len(normal)):
        cu.append(c)


    for v in normal:
        vez = choice(cu)
        cu.remove(vez)
        pera[vez] = v
  #  print(pera)

    return ''.join(pera)







while True:
    pal = input('\nInsira uma palavra (0 para parar)\nR: ').strip()
    if pal == '0':
        break
    print('{} embaralhado: \033[36m{}\033[m'.format(pal, embaralhe(pal)))