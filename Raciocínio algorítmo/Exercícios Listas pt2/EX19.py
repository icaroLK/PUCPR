W = []
U = []
L = []
N = []
M = []
O = []
tot = [W,U,L,N,M,O]
porcentagens = []

resp = ''
votos = 0


print('''Qual a melhor Sistema Operacional para uso em servidores?

1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - MAC OS
6 - Outro
0 - Sair''')
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

print(tot)
print(porcentagens)

print('_'*35)
print('{:<19}{:>10}{:>6}'.format('Sistema operacional', 'Votos', '%'))
print('⁻'*35)

for c in tot:
    print('{:<19}{:>10}{:>6}'.format('oi',sum(tot),'po' ))