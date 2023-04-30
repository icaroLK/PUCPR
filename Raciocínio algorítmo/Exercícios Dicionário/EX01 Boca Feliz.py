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


def est():
    a = ['Pão', 'Hamburguer', 'Tomate', 'Bacon', 'Ovo']
    print('_'*32)
    print('{:^40}'.format('\033[97mSITUAÇÃO DO ESTOQUE\033[m'))
    print('⁻'*32)
    for i, c in enumerate(estoque):
        print('  {:<20}qtd:{:>4}'.format(c, estoque[a[i]]))
    print('_'*32)


estoque = {'Pão': 10,
           'Hamburguer': 12,
           'Tomate': 5,
           'Bacon': 5,
           'Ovo': 5}

cardapio = {
    'X-burguer': ['Pão', 'Hamburguer'],
    'X-salada': ['Pão', 'Hamburguer', 'Tomate'],
    'X-bacon': ['Pão', 'Hamburguer', 'Tomate', 'Bacon'],
    'X-egg': ['Pão', 'Hamburguer', 'Ovo'],
    'X-tudo': ['Pão', 'Hamburguer', 'Tomate', 'Hamburguer', 'Bacon', 'Ovo']
}


p = [0] * len(cardapio)
pedidos = [0] * len(cardapio)
pr = [0] * len(cardapio)

preco = [15.99, 15.99, 17.99, 12.99, 19.99]
menu = [cardapio, preco]


print('_'*32)
print('{:^40}'.format('\033[97mCARDÁPIO\033[m'))
print('⁻'*32)
for i, c in enumerate(menu[0]):
    print('  {:<20}R${:>6}'.format(c, menu[1][i]))
print('_'*32)
print("0. Sair")
print('1. Estoque')
print('⁻'*32)


print("O que deseja pedir?\n")

while True:
    resp = input("R: ").strip().replace('-', '').title()
    acabou = 0
    if resp == '0':
        break
    elif resp == '1':
        est()

    elif resp[:3] in 'Xbu':
        if consult(0) != 1:
            p[0] += 1
            if p[0] == 1:
                pedidos[0] = 'X-burguer'
                pr[0] = 15.99

    elif resp[:3] in 'Xsa':
        if consult(1) != 1:
            p[1] += 1
            if p[1] == 1:
                pedidos[1] = 'X-salada'
                pr[1] = 15.99
    elif resp[:3] in 'Xba':
        if consult(2) != 1:
            p[2] += 1
            if p[2] == 1:
                pedidos[2] = 'X-bacon'
                pr[2] = 17.99
    elif resp[:3] in 'Xeg':
        if consult(3) != 1:
            p[3] += 1
            if p[3] == 1:
                pedidos[3] = 'X-egg'
                pr[3] = 12.99
    elif resp[:3] in 'Xtu':
        if consult(4) != 1:
            p[4] += 1
            if p[4] == 1:
                pedidos[4] = 'X-tudo'
                pr[4] = 19.99
    else:
        print('Item não localizado no cardápio\n')


for c in range(p.count(0)):
    p.remove(0)
for c in range(pedidos.count(0)):
    pedidos.remove(0)
for c in range(pr.count(0)):
    pr.remove(0)


print('\n\n')
print('_'*33)
print('{:^40}'.format('\033[97mCONTA\033[m'))
print('⁻'*33)
print('  {:<11}{:>5}  {:>11}\n'.format('Item', 'Qtd', 'Preço'))


tot = 0
for c in range(len(p)-p.count(0)):
    print('  {:<11}{:>5}     R$\033[32m{:>6}\033[m'.format(
        pedidos[c], p[c], pr[c]))
    tot += pr[c] * p[c]

print('_'*33)
print('  {:<11}{:>5}     R$\033[32m{:>6.2f}\033[m'.format(
    'Total', sum(p), tot))


print('\n\n\n')
