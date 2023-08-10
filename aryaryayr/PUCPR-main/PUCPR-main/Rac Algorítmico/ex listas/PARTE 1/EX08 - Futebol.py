team = []
for c in range(4):
    name = str(input(f'Digite o nome do {c+1}º time: ')).upper()
    team.append(name)

pontos = [0] * 4
for t1 in range(4):
    for t2 in range(t1+1, 4):
        print(f'\033[1;35m{team[t1]}\033[m x \033[1;34m{team[t2]}\033[m')
        g1 = int(input(f'Gols do \033[1;35m{team[t1]}\033[m: '))
        g2 = int(input(f'Gols do \033[1;34m{team[t2]}\033[m: '))
        if g1 > g2:
            pontos[t1] += 3
        elif g2 > g1:
            pontos[t2] += 3
        else:
            pontos[t1] += 1
            pontos[t2] += 1

best = max(pontos)
camp = [team[t1] for t1 in range(4) if pontos[t1] == best]
if len(camp) == 1:
    print(f'\033[1;36mCAMPEÃO: TIME {camp[0]}\033[m')
else:
    print('HOUVE UM EMPATE!')
    for time in camp:
        print(time)
