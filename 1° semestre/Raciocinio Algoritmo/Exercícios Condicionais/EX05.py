print('\033[1m{}'.format('—')*65)
print('\033[1m{:^65}\033[m'.format("PASSAGENS DE AVIÃO PARA OS ESTADOS BRASILEIROS"))
print('\033[1m{}\033[m'.format('—')*65)
print('\n')
print('\033[1m{}'.format('—')*65)
print('''     \033[1mDESTINO\033[m                      \033[1mIDA\033[m                \033[1mIDA E VOLTA\033[m
  
[1] Região Norte................R$500,00................R$900,00
[2] Região Nordeste.............R$350,00................R$650,00
[3] Região Centro-Oeste.........R$350,00................R$600,00
[4] Região Sul..................R$300,00................R$550,00''')
print('\033[1m{}\033[m'.format('—')*65)


dest = int(input('\nInsira seu destino: '))
cond = int(input('\nEscolha uma forma de passagem:\n\n[1] IDA\n[2] IDA E VOLTA\n\nR: '))

if dest == 1 and cond == 1:
    print('Você viajará para a Região Norte e pagará R$500,00')
if dest == 1 and cond == 2:
    print('Você viajará para a Região Norte e pagará R$900,00')

if dest == 2 and cond == 1:
    print('Você viajará para a Região Nordeste e pagará R$350,00')
if dest == 2 and cond == 2:
    print('Você viajará para a Região Nordeste e pagará R$650,00')

if dest == 3 and cond == 1:
    print('Você viajará para a Região Centro-Oeste e pagará R$350,00')
if dest == 3 and cond == 2:
    print('Você viajará para a Região Centro-Oeste e pagará R$600,00')

if dest == 4 and cond == 1:
    print('Você viajará para a Região Sul e pagará R$300,00')
if dest == 4 and cond == 2:
    print('Você viajará para a Região Sul e pagará R$550,00')
