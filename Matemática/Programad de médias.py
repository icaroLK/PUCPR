def titulo(msg):
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format(msg))
    print('\033[1;97m{}\033[m'.format('—')*40)


def leiaint(a):
    try:
        if int(a) > 2 or int(a) < 1:
            a = leiaint(input('Insira uma opção válida\nR: '))
        resp = int(a)
        return int(a)

    except ValueError:
        a = leiaint(input(
            '\033[31mDados inválidos!!!\033[m Insira um número inteiro válido\nR: '))
        resp = int(a)
        return int(a)


titulo('CALCULADORA DE MÉDIA')
resp = input('1 OU 2:')

leiaint(resp)


if resp in '1':
    print('oi')
if resp in '2':
    print('tchau')