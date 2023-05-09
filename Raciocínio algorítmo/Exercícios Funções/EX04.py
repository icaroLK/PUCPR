def func(a):
    if a > 0:
        return 'P'
    elif a < 0:
        return 'N'
    else:
        return '0'







resp = int(input('Insira um número: '))
print(func(resp))