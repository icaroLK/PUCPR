num = input('Insira um número: ')
for c in range(len(num)):
    print('{} x 10^{}'.format(num[c], len(num)-(c+1)), end='')
    if c <= len(num) - 2:
        print(' + ', end='')
    else:
        print('')
