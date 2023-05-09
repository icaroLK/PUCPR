print('_' * 40)
print('\033[97m{:^40}\033[m'.format('Invero de um número'))
print('⁻' * 40)


def rev(a):
    inver = []
    for c in range(len(a), 0, -1):
        inver.append(a[c-1])
    return ''.join(inver)



num = int(input('Insira um número: '))
print(f'{num} |', rev(str(num)))
print('\n\n')