nomes = []
G1 = G2 = G3 = G4 = 0
temp = []
champ = ''
cu = []
alu = 0
for c in range(31, 34+1):
    resp = input('Insira o nome do {}° time: '.format(c-30)).strip().title()
    pera = '\033[{}m{}\033[m'.format(c, resp)
    nomes.append(pera)


for c in range(4):
    temp = nomes.copy()
    temp.pop(c)
#    print(temp)
    for oi in temp:
        alu += 1
        print('\nPARTIDA {}'.format(alu))
        print(f'{nomes[c]} x {oi}')
        cu = []
        cu.append(nomes[c])
        cu.append(oi)
        for lsd in cu:
            P1 = 0
            P2 = 0
            P = int(input(f'Gols do {lsd}: '))
            if lsd == nomes[0]:
                G1 += P
            elif lsd == nomes[1]:
                G2 += P
            elif lsd == nomes[2]:
                G3 += P
            elif lsd == nomes[3]:
                G4 += P
    


#print(f'{G1}       {G2}       {G3}         {G4}     ')
print()
print("="*6, "\033[97mFIM DO CAMPEONATO!!!\033[m", "="*6)
print()

if G1 > G2 and G1 > G3 and G1 > G4:
    print(f'\033[32mVencedor!!!\033[m\nTime {nomes[0]} com {G1} gols')
elif G2 > G1 and G2 > G3 and G2 > G4:
    print(f'\033[32mVencedor!!!\033[m\nTime {nomes[1]} com {G2} gols')
elif G3 > G2 and G3 > G1 and G3 > G4:
    print(f'\033[32mVencedor!!!\033[m\nTime {nomes[2]} com {G3} gols')
elif G4 > G2 and G4 > G3 and G4 > G1:
    print(f'\033[32mVencedor!!!\033[m\nTime {nomes[3]} com {G4} gols')
else:
    print('\033[33mEMPATE!!!\033[m\nNão houve vencedores')