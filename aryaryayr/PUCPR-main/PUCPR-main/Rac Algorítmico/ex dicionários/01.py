def analise(x):
    a = ['xburguer', 'xsalada', 'xbacon', 'xegg', 'xtudo']
    acabou = 1
    for c in cardapio[a[x]]:
        if estoque[c] == 0:
            print(f'\033[1;33mInfelizmente acabou o {c}\033[m')
            acabou = 0
            return 1
        else:
            estoque[c] -= 1
    if acabou == 1:
        print(f'Um {a[x][0].title()}-{a[x][1:].title()} saindo no capricho!')



estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
 'xburguer': ['pao', 'hamburguer'],
 'xsalada': ['pao', 'hamburguer', 'tomate'],
 'xbacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
 'xegg': ['pao', 'hamburguer', 'ovo'],
 'xtudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo'],
}

cont = 1
print('—'*40)
print(f'{"CARDÁPIO BOCA FELIZ":^40}')
print('—'*40)
for sanduiche, ingredientes in cardapio.items():
    print(f'[{cont}] {sanduiche[0].title()}-{sanduiche[1:].title():<10}  -    ', end='')
    for c in range(len(ingredientes)):
        print(f'{ingredientes[c].title()}, ', end='')
    print()
    cont += 1
print(f'[{cont}] Estoque')
print('—'*40)

while True:
    ans = input('O que deseja pedir? [0 p/ parar] ').lower().replace('-', '')
    if ans in '0' or ans in 'sair':
        break
    if ans in 'estoque' or ans in '6':
        print('—'*40)
        print(f'{"ESTOQUE":^40}')
        print('—'*40)
        for i, v in estoque.items():
            print(f'{i.title():<12}  -  {v:>6}')

    elif ans not in cardapio and ans not in 'estoque' and ans not in '123456':
        print('\033[1;31mERRO! Item não econtrado.\033[m')
    else:
        if ans in 'xburguer' or ans in '1':
            analise(0)

        elif ans in 'xsalada' or ans in '2':
            analise(1)

        elif ans in 'xbacon' or ans in '3':
            analise(2)

        elif ans in 'xegg' or ans in '4':
            analise(3)

        elif ans in 'xtudo' or ans in '5':
            analise(4)
