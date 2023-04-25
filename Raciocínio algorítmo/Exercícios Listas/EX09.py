from random import choice
esc = [0,1,2,3]

nomes = []
tempnom = []
gols = []

for c in range(1, 4+1):
    resp = input('Insira o nome do {}° time: '.format(c))
    nomes.append(resp)

tempnom = nomes.copy()


for c in range(1, 4+1):
    print(f'{c}° PARTIDA')

    opa = choice(tempnom)

    
    tempnom.pop(tempnom.index(opa)) # tenho que colocar a posicção que o opa ta

    opa2 = choice(tempnom)
    tempnom.pop(tempnom.index(opa2))
    print(opa, 'X', opa2)