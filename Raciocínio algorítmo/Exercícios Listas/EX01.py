num = []
maior = []
menor = []
s = 0

for c in range(1, 6+1):
    n = float(input('Insira o {}° número: '.format(c)))
    s += n
    num.append(n)
m = s/6
print('Média dos números digitados: {:.1f}'.format(m))

for c in num:
    if c > m:
        maior.append(c)
    elif c < m:
        menor.append(c)
#print(num)
print('Números maiores que a média: {}'.format(maior))
print('Números menores que a média: {}'.format(menor))