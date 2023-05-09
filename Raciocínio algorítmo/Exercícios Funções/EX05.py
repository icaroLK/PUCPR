def somaimposto(taxa, custo):
    preco = custo + (custo/100) * taxa
    return preco


custo = float(input('Insira o custo: R$'))
taxa = float(input('Insira a taxa: '))
print('Preço: R$', end='')
print('{:.2f}'.format(somaimposto(taxa, custo)))