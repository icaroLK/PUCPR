#FODASE ESSE VOU RECOMEÇAR OUTRO DPS


def titulo(msg):
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format(msg))
    print('\033[1;97m{}\033[m'.format('—')*40)


def notas(a):
    try:
        if int(a) > 2 or int(a) < 1:
            a = notas(input('Insira uma opção válida\nR: '))
        resp = int(a)
        return int(a)

    except ValueError:
        a = notas(input(
            '\033[31mDados inválidos!!!\033[m Insira um número inteiro válido\nR: '))
        resp = int(a)
        return int(a)

def leiaint(a):
    try:
        return int(a)

    except ValueError:
        a = leiaint(input(
            '\033[31mDados inválidos!!!\033[m Insira um número inteiro válido\nInsira um número inteiro: '))
        return int(a)



def leianota(msg):
    while True:
        r = msg.replace(',','.')
        if r.replace('.','').replace(',','').isnumeric() == True:
            num = float(r)
            break
        else:
            print('\033[31mDADOS INVÁLIDOS.\033[m Tente novamente')
            break
    return num



notass = []
nt = 0

titulo('CALCULADORA DE MÉDIA')
resp = input('1 - Média aritmética\n2 - Média ponderada\nR: ')
notas(resp)


if resp in '1':  #média aritmética:
    titulo('Média aritmética')
    qtd = leiaint(input('Insira a quantidade de notas: '))
    for c in range(qtd):
        nota = leianota(input('Insira a nota da {}° prova: '.format(c+1))) #aqui voce pode digitar tanto com virgula tanto com ponto
        nt += nota
    m = nt / qtd







if resp in '2':
    print('tchau')





print('\nA sua média foi {:.1f}'.format(m))