def salario(x):
    y = 0.9*x + 200
    return y

while True:
    vendas = int(input('Quantas vendas você realizou? '))
    print(f'{salario(vendas)}')
    ans = str(input('Deseja continuar? ')).strip().upper()[0]
    if ans in 'N':
        break