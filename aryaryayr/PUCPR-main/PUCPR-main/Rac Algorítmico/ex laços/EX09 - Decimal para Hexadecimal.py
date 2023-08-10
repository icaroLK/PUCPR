#cabeçalho
print('—'*40)
print(F'{"DECIMAL PARA HEXA":^40}')
print('—'*40)
# coletando info e calculando
l = []
h = []
while True:
    l.clear()
    h.clear()
    dec = int(input('Digite o número em decimal: '))
    print('~' * 40)
    print(f'{"Dividir por 16 até o quociente ser 0"}')
    print('~' * 40)
    d2 = dec
    quo = 0
    res = 0
    while True:
        quo = dec // 16
        res = dec % 16
        dec = quo
        l.append(res)
        if quo == 0:
            break
    print('RESTOS:')
    for i, v in enumerate(l):
        v2 = str(v)
        v3 = v2.replace('10', 'A').replace('11', 'B').replace('12', 'C')\
            .replace('13', 'D').replace('14', 'E').replace('15', 'F')
        h.append(v3)
        print(f'{v} -> {v3}')
    l.reverse()
    # mostrando resultados
    print(f'O número \033[1;34m{d2}\033[m em Hexadecimal é ', end='')
    for i, v in enumerate(reversed(h)):
        print(f'\033[1;34m{v}', end='')
    print('(h)\033[m')
    ans = str(input('Deseja continuar? [S/N] ')).upper()
    if ans in 'N':
        break