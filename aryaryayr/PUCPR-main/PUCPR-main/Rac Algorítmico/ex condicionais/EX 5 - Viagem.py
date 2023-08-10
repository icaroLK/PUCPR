# cabeçalho
print('—'*40)
print(f'{"Compra de Passagens":^40}')
print('—'*40)
# coletando informações
print('[1] Região Norte')
print('[2] Região Nordeste')
print('[3] Região Centro-Oeste')
print('[4] Região Sul')
dest = int(input('Pra onde você quer viajar? '))
ret = str(input('Você gostaria da passagem de ida e volta? [S/N] ')).upper()
# calculando e mostrando resultados
if dest == 1:
    if ret in 'NAO':
        print('Sua passagem vai custar R$500,00')
    if ret in 'SIM':
        print('Sua passagem vai custar R$900,00')
if dest == 2:
    if ret in 'NAO':
        print('Sua passagem vai custar R$350,00')
    if ret in 'SIM':
        print('Sua passagem vai custar R$650,00')
if dest == 3:
    if ret in 'NAO':
        print('Sua passagem vai custar R$350,00')
    if ret in 'SIM':
        print('Sua passagem vai custar R$600,00')
if dest == 4:
    if ret in 'NAO':
        print('Sua passagem vai custar R$300,00')
    if ret in 'SIM':
        print('Sua passagem vai custar R$550,00')