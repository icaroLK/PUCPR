from random import randint


jogos = []

for c in range(100):
    n = randint(1, 6)
    jogos.append(n)

for c in range(1, 6+1):
    print(f'O número {c} caiu {jogos.count(c)} vezes')
