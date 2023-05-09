def func(a):
    for linha in range(1, resp+1):
        for c in range(1, linha+1):
            print(c, end=' ')
        print()

resp = int(input('Insira um número: '))
func(resp)


