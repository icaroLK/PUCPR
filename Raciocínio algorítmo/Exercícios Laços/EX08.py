print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("CALCULADORA DE BINÁRIO PRA DECIMAL"))
print('\033[1m{}\033[m'.format('—')*40)


num = input('Insira um número em binário: ')
posini = num.find('1')
num = num[posini:]          #caso os primeiros digitos sejam zero, ele desconsidera e pega o primeiro 1 que tiver
qtd = len(num)
vez = resp = 0
for c in range(qtd):
    elev = 2 ** ((qtd - 1) - vez)
    if c != qtd and num[c] == '1':
        resp += elev
    vez += 1
print(resp)
