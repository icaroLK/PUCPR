Windows = []
Unix = []
Linux = []
Netware = []
Mac = []
Outro = []
tot = [Windows, Unix, Linux, Netware, Mac, Outro]
porcentagens = []
servers = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
resp = ''
votos = 0

print('Qual é o melhor Sistema Operacional para uso em servidores?')

for c in range(1, 6+1):
    if c == 6:
        print('0 - Sair')
    else:
        print(f'{c} - {servers[c-1]}')


while resp != '0':
    while True:
        resp = input('R: ')
        if resp == '0':
            break
        try:
            num = int(resp)
            if num > 6 or num < 1:
                print('Opção inválida')
            else:
                votos += 1
                break
        except ValueError:
            print('Digite um número')

    for c in range(1, 6+1):
        if num == c:
            tot[c-1].append(1)

for i, per in enumerate(tot):
    porce = int('{:.0f}'.format(len(per)/votos*100))
    porcentagens.append(porce)



print('_'*42)
print('   {:<19}{:>10}{:>7}'.format('Sistema operacional', 'Votos', '%'))
print('⁻'*42)


for i,c in enumerate(tot):
    print('   {:<19}{:>10}{:>6}%'.format(servers[i], sum(tot[i]), porcentagens[i]))
print('_'*42)
print('   {:<19}{:>10}{:>7}'.format('Total', votos, '100%'))