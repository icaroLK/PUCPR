from random import randint

val = []
def dado(qnt):
    for c in range(qnt):
        num = randint(1, 6)
        val.append(num)
    print(val)
    for c in range(1, 7):
        count = val.count(c)
        print(f'O número {c} aparece {count} vezes.')


qnt = int(input('Quantas vezes quer jogar o dado? '))
dado(qnt)