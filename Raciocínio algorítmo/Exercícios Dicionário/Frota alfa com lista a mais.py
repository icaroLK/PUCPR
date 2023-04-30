#usando mais uma lista

def tit(msg, x=40):
    print('_' * x)
    print('\033[97m{:^40}\033[m'.format(msg))
    print('⁻' * x)


def conferir_opc(msg, a, b, erro1='Insira um número', erro2='Insira uma opção válida'):
    global opc
    while True:
        resp = input(msg).strip()
        try:
            opc = int(resp)
            if opc < a or opc > b:
                print(erro2)
            else:
                return opc
        except ValueError:
            print(erro1)


def conferir_num(msg, erro='Insira um número'):
    global valor
    while True:
        resp = input(msg).strip().replace(',','.')
        try:
            valor = float(resp)
            return valor
        except ValueError:
            print(erro)

anos_luz = {'\033[31mpc\033[m': 0.31,
            '\033[32mal\033[m': 1,
            '\033[33mae\033[m': 63241.09,
            '\033[34mml\033[m': 525960.23,
            '\033[35msl\033[m': 31557609.92
            }

unidades = ['Parsec (\033[31mpc\033[m)',
            'Ano-luz (\033[32mal\033[m)',
            'Unidade Astronômica (\033[33mae\033[m)',
            'Minuto-Luz (\033[34mml\033[m)',
            'Segundo-Luz (\033[35msl\033[m)'
            ]


tit('Unidades de conversão')
for i, c in enumerate(unidades):
    print(f'  {i+1}. {c}')
print('_' * 40)

conferir_num('Valor a ser convertido: ')
a = ['', '\033[31mpc\033[m', '\033[32mal\033[m', '\033[33mae\033[m', '\033[34mml\033[m', '\033[35msl\033[m'] #não precisaria desse lista se eu soubesse pegar o nome de um chave em um dicionário

conferir_opc('Converter de: ', 1,5)
de = opc

conferir_opc('Converter para: ',1,5)
para = opc

final = valor * anos_luz[a[para]] / anos_luz[a[de]]
print('\nConversão:\n{} {} = {:.4f} {}\n\n'.format(valor,a[de],final,a[para]))

