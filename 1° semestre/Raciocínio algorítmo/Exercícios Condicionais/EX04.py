print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("LOJINHA"))
print('\033[1m{}\033[m'.format('—')*40)


p = float(input('\nInsira o preço da compra: R$'))
f = str(input('''Escolha a forma de pagamento:

[1] á vista no dinheiro/cheque (10% de desconto)
[2] á vista no cartão (15% de desconto)
[3] até 2x no cartão (sem desconto)
[4] 3x ou mais no cartão (10% de juros)\nR: ''')).strip()




if f == '1':
    print('''Você pagará á vista e terá um desconto de \033[32m10%\033[m equivalente á \033[32mR${:.2f}\033[m
O preço final ficará \033[32mR${:.2f}\033[m'''.format(p*10/100, p-(p*10/100)))


elif f == '2':
    print('''O pagamento no cartão á vista tem um desconto de \033[32m5%\033[m equivalente a \033[32mR${:.2f}\033[m
O preço final ficará \033[32mR${:.2f}\033[m'''.format(p*15/100, p-(p*15/100)))
elif f == '3':
    print('''O parcelamento até 2x no cartão \033[31mnão\033[m permite descontos.
O preço fincal ficará \033[32mR${}\033[m'''.format(p))
elif f == '4':
    print('Com o parcelamento em 3x ou mais, é aplicado um \033[31mjuros\033[m de \033[33m20%\033[m')
    c = int(input('Você pagará em quantas parcelas? '))
    print('\nO preço final será \033[32mR${:.2f}\033[m divididos em {} '
          'parcelas de \033[32mR${:.2f}\033[m'.format((p+(p*20/100)), c, (p+(p*20/100))/c))
