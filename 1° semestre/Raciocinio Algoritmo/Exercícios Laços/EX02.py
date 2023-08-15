print('\033[1m{}'.format('—')*58)
print('\033[1m{:^40}\033[m'.format("Números entre 1000 e 1999 que divididos por 11 dão resto 5"))
print('\033[1m{}\033[m'.format('—')*58)

c = 1000
linha = 0
while c <= 1999:
    if c % 11 == 5:
        print(c, end=' / ')

        linha += 1
        if linha == 14 or linha == 28 or linha == 42 or linha == 56 or linha == 70 or linha == 84:
            print('')
    c += 1
print('Cabo')