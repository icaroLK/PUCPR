print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("CALCULADORA DO PESO IDEAL"))
print('\033[1m{}\033[m'.format('—')*40)

alt = float(input('Insira sua altura (cm): '))
ideal = sex = ' '

while sex not in 'MF':
    sex = input('Insira seu sexo (M/F): ').strip().title()[0]
    if sex in 'MF':
        break
    print('\033[31mDados inválidos.\033[m Insira novamente')

if sex in 'M':
    ideal = (72.7 * alt / 100) - 58
if sex in 'F':
    ideal = (62.1 * alt / 100) - 44.7

print('O seu peso ideal é {:.2f}kg'.format(ideal))
