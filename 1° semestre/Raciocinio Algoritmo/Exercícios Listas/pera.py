nomes = []
G1 = G2 = G3 = G4 = 0
temp = []
champ = ''
cu = []
alu = 0
for c in range(1, 4+1):
    resp = input('Insira o nome do {}° time: '.format(c)).strip().title()
    nomes.append(resp)


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
    

print(f'{G1}       {G2}       {G3}         {G4}     ')



   #     P2 = int(input(f'Gols do {oi}'))


