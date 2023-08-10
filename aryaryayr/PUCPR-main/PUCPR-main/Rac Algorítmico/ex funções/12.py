from random import randint
from time import sleep

def embaralha(name):
    l = []
    while True:
        num = randint(0, len(name)-1)
        name.count(name[num])
        if name.count(name[num]) > l.count(name[num]) :
            l.append(name[num])
        if len(l) == len(name):
            break
    print('Resultado: ', end='')
    for c in range(len(l)):
        print(f'{l[c]}', end='')


pal = str(input('Digite uma palavra: ')).lower()
print('Embaralhando...')
sleep(1)
embaralha(pal)