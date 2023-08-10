opt = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
vote = []
qnt = []
porc = []

print('[1] Windows Server\n'
      '[2] Unix\n'
      '[3] Linux\n'
      '[4] Netware\n'
      '[5] Mac OS\n'
      '[6] Outro\n')
while True:
    ans = int(input('Qual o melhor Sistema Operacional? [0 p/ parar] '))
    if ans < 0 or ans > 6:
        print('ERRO! Digite um valor válido.')
    elif ans == 0:
        break
    else:
        vote.append(ans)
vote.sort()

for c in range(1, 7):
    num = vote.count(c)
    qnt.append(num)

for c in range(6):
    p = f'{qnt[c] / len(vote) * 100:.1f}'
    porc.append(p)

print('\033[1;35m—\033[m'*41)
print(f'\033[1;35m{"Sistema Operacional":<10}{"Votos":>10}{"%":>9}\033[m')
print('\033[1;35m—\033[m'*41)
for c in range(6):
    print(f'{opt[c]:<10}\t{qnt[c]:>11}{porc[c]:>12}%')
print('\033[1;35m—\033[m'*41)
print(f'\033[1;35m{"TOTAL":<10}{sum(qnt):>17}{"100%":>13}\033[m')
        