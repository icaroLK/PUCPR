def comeq(cu):
    titulo(cu)
    print('\033[34m')
    resp = help(cu)
    print('\033[m')


def titulo(msg, cor=0):
    print('\033[1;97m—'*(len(msg)+6))
    print('   {}'.format(msg))
    print('—'*(len(msg)+6), '\033[m')


while True:
    duvida = input('Insira o comando que deseja saber como funciona (digite FIM para parar): ').strip()
    if duvida.upper()[:3] in 'FIM':
        print('Obrigado, volte sempre :)')
        break
    else:
        comeq(duvida)
