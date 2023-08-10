def ler(num):
    count = 0
    for i in num:
        count += 1
    return count

num = int(input('Digite um número: '))
num = str(num)
print(f'O número {num} tem {ler(num)} casas')