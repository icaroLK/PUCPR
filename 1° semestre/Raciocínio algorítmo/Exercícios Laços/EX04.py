print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("LISTA EM ORDEM CRESCENTE"))
print('\033[1m{}\033[m'.format('—')*40)

list = []
for c in range(5):
    n = int(input('Insira um número: '))
    list.append(n)
list.sort()
print('Os números digitado em ordem crescente ficam: ', end='')
for c in range(len(list)):
    print(list[c], end=' ')