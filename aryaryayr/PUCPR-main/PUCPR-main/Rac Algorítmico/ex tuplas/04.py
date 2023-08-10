prod = {}

while True:
    produto = str(input('Digite o produto: '))
    if produto in prod:
        ans = str(input('Esse produto já está cadastrado. Deseja a tualiar o preço? ')).strip().upper()[0]
        if ans in 'N':
            continue
        else:
            pass
    preco = float(input('Digite o preço: '))
    prod[produto] = preco
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    print('—' * 30)
    if cont in 'N':
        break

print('LISTA DE ITENS')
for produto, preco in prod.items():
    print(f'{produto} - R${preco:.2f}')