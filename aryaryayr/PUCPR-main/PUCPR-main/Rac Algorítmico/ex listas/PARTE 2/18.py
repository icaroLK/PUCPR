vote = []
porc = []
qnt = []
sem_rep = []

while True:
    n = int(input('Número do jogador [0 p/ parar]: '))
    if n > 23 or n < 0:
        print('ERRO! Digite um jogador existente (1 - 23).') 
    elif n == 0:
        break
    else:
        vote.append(n)

vote.sort()
sem_rep.sort()
print()
print(f'Foram computados {len(vote)} votos.')
print('\033[1;35m—\033[m'*27)
print(f'\033[1;35m{"Jogador":<10}{"Votos":>6}{"%":>8}\033[m')
print('\033[1;35m—\033[m'*27)

for c in range(1, 23):
    num = vote.count(c)
    if num != 0:
        qnt.append(num)

for c in range(len(vote)):
    if vote[c] not in sem_rep:
        sem_rep.append(vote[c])

for c in range(len(qnt)):
    p = f'{qnt[c] / len(vote) * 100:.1f}'
    porc.append(p)

for c in range(len(sem_rep)):
    print(f'  {sem_rep[c]:<8}{qnt[c]:>4}{porc[c]:>12}%')