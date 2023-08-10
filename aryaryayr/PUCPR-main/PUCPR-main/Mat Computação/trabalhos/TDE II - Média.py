print('–' * 40)
print(f'{"CALCULADORA DE MÉDIAS":^40}')
print('–' * 40)

l = []
p = []
m = []
print('[1] Média Aritmética\n'
      '[2] Média Ponderada\n'
      '[3] Quanto falta pra passar')
while True:
    l.clear()
    p.clear()
    m.clear()
    print('~' * 40)
    typ = int(input('Qual tipo de média deseja calcular? [999 p/ parar] '))
    if typ == 999:
        break
    if typ == 3:
        med2 = input('Digite a média pra passar: ').replace(',', '.')
        med = float(med2)
        qnt = int(input('Quantas notas existem no total? '))
        for c in range(0, qnt - 1):
            score2 = input(f'Digite a {c+1}ª nota: ').replace(',', '.')
            score = float(score2)
            l.append(score)
        ans = str(input('Existem pesos? ')).strip().upper()[0]
        if ans in 'N':
            print('~' * 40)
            print('( ', end='')
            for c in range(0, len(l)):
                if c != len(l) - 1:
                    print(f'{l[c]} + ', end='')
                elif c == len(l) - 1:
                    print(f'{l[c]} + n) / {len(l)+1} = 7,0')
            print(f'n = {med} * {len(l)+1} - {sum(l)}')
            math = (med * (len(l)+1)) - sum(l)
            print(f'\033[1;36mPara passar, o aluno deve tirar a nota {math:.1f}\033[m')
        else:
            for c in range(qnt):
                peso = int(input(f'Digite o {c+1}º peso: '))
                p.append(peso)
            print('( ', end='')
            for c in range(0, len(l)):
                if c != len(l) - 1:
                    mult = l[c]*p[c]
                    print(f'{mult} + ', end='')
                    m.append(mult)
                elif c == len(l) - 1:
                    mult = l[c]*p[c]
                    print(f'{l[c]*p[c]} + n x {p[c+1]}) = {sum(p) * med}')
                    m.append(mult)
            n = ((sum(p) * med) - sum(m)) / p[len(l)]
            print(f'n = {sum(p) * med} - {sum(m)} / {p[len(l)]}')
            print(f'\033[1;36mPara passar, o aluno deve tirar a nota {n:.1f}\033[m')
    elif typ > 3 or typ == 0 and typ != 999:
        print('\033[1;31mERRO! Digite uma escolha válida.\033[m')
    else:
        num = int(input('Quantas notas quer calcular? '))
        for c in range(num):
            score2 = input(f'Digite a {c+1}ª nota: ').replace(',', '.')
            score = float(score2)
            l.append(score)
        if typ == 1:
            print('~' * 40)
            for c in range(0, len(l)):
                if c != len(l) - 1:
                    print(f'{l[c]} + ', end='')
                elif c == len(l) - 1:
                    print(f'{l[c]} = {sum(l)} / {len(l)}')
            ma = sum(l) / len(l)
            print(f'\033[1;36mMÉDIA ARITMÉTICA: {ma:.1f}\033[m')
            if ma >= 7:
                print('Você \033[1;32mPASSOU!\033[m')
            else:
                print('Você está de \033[1;34mRECUPERAÇÃO!\033[m')           
        elif typ == 2:
            for c in range(num):
                pon = int(input(f'Digite o peso da {c+1}ª nota: '))
                p.append(pon)
            print('~' * 40)
            for c in range(0, len(l)):
                mult = l[c] * p[c]
                m.append(mult)
                if c != len(l) - 1:
                    print(f'{l[c] * p[c]} + ', end='')
                elif c == len(l) - 1:
                    print(f'{l[c] * p[c]} = {sum(m)} / {sum(p)}')
            mp = sum(m) / sum(p)
            print(f'\033[1;36mMÉDIA PONDERADA: {mp:.1f}\033[m')
            if mp >= 7:
                print('Você \033[1;32mPASSOU!\033[m')
            else:
                print('Você está de \033[1;34mRECUPERAÇÃO!\033[m')
        else:
            print('\033[1;31mERRO! Digite uma escolha válida.\033[m')
print('–' * 40)
print(f'{"FIM":^40}')