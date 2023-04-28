lista = []

while True:
    n = float(input('Insira um valor [-1 para parar]: '))
    if n == -1:
        break
    lista.append(n)

print(f'Quantidade de valores: {len(lista)}')



print('\nValores em ordem: ', end='')
for c in lista:
    print(c, end=' / ')




print('\nValores em ordem invertida: ')
for c in range(len(lista)-1, -1, -1):
    print(lista[c])

print(f'\n\nA soma dos valores é {sum(lista)}')

m = sum(lista)/len(lista)

print(f'\nA média dos valores é {m}')

print('\nValores acima da média: ')
for c in lista:
    if c > m:
        print(c)

print('\nValores abaixo de sete: ')
for c in lista:
    if c < 7:
        print(c)

print('Cabo :)')