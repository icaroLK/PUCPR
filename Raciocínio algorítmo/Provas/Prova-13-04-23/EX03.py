# Exercício 3: 

num = int(input('Insira um número: '))
res = 0
c = 0
while True:
    c += 1
    if num % c == 0:
        res += c
    if c >= num // 2:
        if res == num:
            print('O número {} é um número perfeito'.format(num))
            break
        else:
            print('O número {} não é um número perfeito'.format(num))
            break
