print('\033[1;35m[1]\033[m n -> 10')
print('\033[1;34m[2]\033[m 10 -> m')
while True:
    ç = int(input('\033[1mQual trasnformação deseja fazer? [999 para parar]\033[m '))
    print('~'*50)
    if ç == 1:
        l = []
        base = int(input('Digite a base \033[1;35moriginal\033[m: '))
        trans = int(input(f'Digite um número na base \033[1;35m{base}\033[m: '))
        num = str(trans)
        cont = len(num)
        pos = 0
        for c in range(0, cont):
            l.append(num[pos])
            pos += 1
            cont -= 1
        l.reverse()
        pos1 = 0
        p = []
        for i, v in enumerate(l):
            k = base ** i
            f = k * v
            o = len(f)
            if v == '0':
                print(f'{base}^{i} = {k} * {v} = 0')
            if v == '1':
                print(f'{base}^{i} = {k} * {v} = {o}')
                pos1 += 1
                p.append(o)
            else:
                if v not in '0':
                    h = int(v)
                    j = k * h
                    print(f'{base}^{i} = {k} * {v} = {j}')
                    p.append(j)

        print(f'O número \033[1;35m{trans}\033[m em decimal é \033[1;35m{sum(p)}\033[m')
        print('~' * 50)

    if ç == 2:
        l = []
        dec = int(input('Digite um número em \033[1;34mDECIMAL\033[m: '))
        bas = int(input('Qual base quer transformar? '))
        d2 = dec
        quo = 0
        res = 0

        while True:
            quo = dec // bas
            res = dec % bas
            dec = quo
            l.append(res)
            if quo == 0:
                break
        print(f'O número \033[1;34m{d2}\033[m em base {bas} é ', end='')
        for i, v in enumerate(reversed(l)):
            print(f'\033[1;34m{v}', end='')
        print(f'{d2 % 2}\033[m')
        print('~' * 50)
    if ç == 999:
        break

print()
print(f'{" FIM ":=^50}')
print('Obrigado por consultar!')