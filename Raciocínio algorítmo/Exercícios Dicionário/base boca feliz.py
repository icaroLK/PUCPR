#cabo a base

def consult(x):
        acabou = 0
        a = ['X-burguer', 'X-salada', 'X-bacon', 'X-egg', 'X-tudo']
        for c in cardapio[a[x]]:
            if estoque[c] == 0:
                print('Infelizmente acabou o ingrediente {}'.format(c))
                acabou = 1
                return 1
            else:
                estoque[c] -= 1
        if acabou == 0:
            print('Um {} saindo no capricho! :)'.format(a[x]))    




estoque = {'pao': 10,
           'hamburguer': 12,
           'tomate': 5,
           'bacon': 5,
           'ovo': 5}

cardapio = {
    'X-burguer': ['pao', 'hamburguer'],
    'X-salada': ['pao', 'hamburguer', 'tomate'],
    'X-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'X-egg': ['pao', 'hamburguer', 'ovo'],
    'X-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

p = [0] * len(cardapio)
print('_'*42)
print('{0}\033[97mCARDÁPIO\033[m{0}'.format(' '*17))
print('⁻'*42)
for i, c in enumerate(cardapio):
#    print('{}. {}'.format(i+1, c))
    print('{}'.format(c))
print('⁻'*42)
print("O que deseja pedir?(ᵈⁱᵍⁱᵗᵉ '⁰' ᵖᵃʳᵃ ᵖᵃʳᵃʳ)\n")
while True:
    resp = input("R: ").strip().replace('-', '').title()
    acabou = 0
    if resp == '0':
        break
    elif resp[:3] in 'Xbu':
        if consult(0) != 1:
            p[0] += 1
    elif resp[:3] in 'Xsa':
        if consult(1) != 1:
            p[1] += 1
    elif resp[:3] in 'Xba':
        if consult(2) != 1:
            p[2] += 1
    elif resp[:3] in 'Xeg':
        if consult(3) != 1:
            p[3] += 1
    elif resp[:3] in 'Xtu':
        if consult(4) != 1:
            p[4] += 1
    else:
        print('Item não localizado no cardápio\n')
print(p)