# cabeçalho
print('—'*40)
print(F'{"BINÁRIO -> DECIMAL":^40}')
print('—'*40)
# coletando info
l = []
bin = int(input('Digite o número em binário: '))
bin2 = str(bin)
cont = len(bin2)
# calculando
print('~' * 40)
for c in range(0, cont):
    l.append(bin2[c])
    cont -= 1
l.reverse()
p = []
for i, v in enumerate(l):
    k = 2 ** i
    f = k * v
    o = len(f)
    if v == '0':
        print(f'2^{i} = {k} x {v} = 0')
    elif v == '1':
        print(f'2^{i} = {k} x {v} = {len(f)}')
        p.append(o)
# apresentando resultados
print('~' * 40)
print(f'O número \033[1;36m{bin}\033[m em decimal é \033[1;36m{sum(p)}\033[m')