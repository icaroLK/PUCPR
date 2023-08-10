def pascal(num):
    for l in range(1, num+1):
        for c in range(1, l+1):
            print(c, end=' ')
        print()


num = int(input('Digite o último número: '))
pascal(num)