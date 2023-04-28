per = ['Telefonou para a vítima?', 'Esteve no local do crime?',
       'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
qtd = 0

for i, v in enumerate(per):
    print(f'{i+1}. {v}')
    r = input('R: ').strip().title()[0]
    if r == 'S':
        qtd += 1


if qtd == 5:
    print('\033[31mASSASSINO\033[m')
elif 3 <= qtd < 5:
    print('\033[36mCúmplice\033[m')
elif qtd == 2:
    print('\033[33mSuspeito\033[m')
else:
    print('Inocente')
