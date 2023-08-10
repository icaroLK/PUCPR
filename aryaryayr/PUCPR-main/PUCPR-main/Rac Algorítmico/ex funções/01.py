def piramide(num):
    for c in range(num):
        print(f'{c+1} ' * (c+1))


num = int(input('Digite o número máximo: '))
piramide(num)