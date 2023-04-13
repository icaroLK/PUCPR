print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format("CALCULADORA DE IMC"))
print('\033[1;97m{}\033[m'.format('—')*40)

peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))

IMC = peso / (altura * altura)
print('\nSeu IMC é {:.1f}\n'.format(IMC))

if IMC < 18.5:
    print('\033[31mAbaixo do peso\033[m')

if 18.5 < IMC < 25:
    print('\033[32mPeso ideal\033[m')

if 25 < IMC < 30:
    print('\033[33mSobrepeso\033[m')

if 30 < IMC < 40:
    print('\033[31mObesidade\033[m')

if 40 < IMC:
    print('\033[31mObesidade mórbida\033[m')
