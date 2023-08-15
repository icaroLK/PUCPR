
def valorPagamento(prest, dias):
    if dias <=0:
        return prest
    else:
        multa = prest + (prest * 3 / 100) + (prest * 0.1 / 100) * dias
        return multa

qtd = 0
totprest = 0

while True:
    valorprest = float(input('\nInsira o valor da prestação: R$'))
    if valorprest == 0:
        break
    atraso = int(input('Insira a quantidade de dias em atraso: '))
    preço = valorPagamento(valorprest, atraso)


    print(f'Você precisará pagar: R$ {preço:.2f}')
    totprest += preço
    qtd += 1

print('_' * 40)
print('\033[97m{:^40}\033[m'.format('Relatório do dia'))
print('⁻' * 40)
print(f'Quantidade de prestações pagas: {qtd}')
print(f'Soma do total das prestações pagas: R$ {totprest:.2f}')