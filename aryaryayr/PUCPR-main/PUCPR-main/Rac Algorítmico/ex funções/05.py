def somaImposto(taxa, custo):
    valor = custo + (custo * (taxa / 100))
    return f'Produto taxado: R${valor:.2f}'


custo = float(input('Digite o preço do produto(R$): '))
taxa = float(input('Digite a taxa de imposto (%): '))
print(somaImposto(taxa, custo))