# cabeçalho
print('—'*40)
print(f"{'LOJINHA BACANA':^40}")
print('—'*40)

# coletando informações
l = []
count = int(input('Quantos produtos deseja comprar? '))
for c in range(0, count):
    prod = float(input(f'Qual o valor do {c+1}º produto? R$'))
    l.append(prod)
sum = sum(l)
print()
print(f'O valor total da compra foi de R${sum:.2f}')
print()
print('[1] À vista (Dinheiro/Cheque) - 10% de desconto!')
print('[2] À vista no cartão de crédito - 15% de desconto!')
print('[3] Em 2x - SEM JUROS')
print('[4] Em 3x - Juros de 10%')
print('~'*40)
pay = int(input('Como deseja pagar? '))
# calculando e mostrando resultados
if pay == 1:
    print(f'Você pagará R${sum - sum * 0.10:.2f}')
elif pay == 2:
    print(f'Você pagará R${sum - sum * 0.15:.2f}')
elif pay == 3:
    print(f'Você pagará duas parcelas de R${sum / 2:.2f}')
elif pay == 4:
    print(f'Você pagará três parcelas de R${(sum + sum * 0.10) / 3:.2f}')