meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tm = []
for c in range(0, 12):
    temp = float(input(f'Digite a temperatura média em {meses[c]}: '))
    tm.append(temp)

ma = sum(tm) / 12
print(f'MÉDIA ANUAL: {ma:.2f}')
print('Meses com temperatura acima da média anual: ', end='')
for c in range(len(tm)):
    if tm[c] >= ma and c < 11:
        print(f'{meses[c]},', end=' ')
    if tm[c] >= ma and c == 11:
        print(f'{meses[c]}.')
