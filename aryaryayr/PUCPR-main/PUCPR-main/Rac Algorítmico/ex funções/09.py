def inverte(num):
    rev = []
    pos = len(num) - 1
    for v in num:
        rev.append(num[pos])
        pos -= 1
    for v in rev:
        print(v, end='')
    print()

num = str(input('Digite um número: '))
print(f'O número invertido fica: ', end='')
inverte(num)