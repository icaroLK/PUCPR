mon = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tm = []
mon_med = []
for c in range(12):
    temp = float(input(f'Digite a temperatura média em {mon[c]}: '))
    tm.append(temp)

tma = sum(tm) / 12
for c in range(12):
    if tm[c] > tma:
        mon_med.append(mon[c])
print(f'MÉDIA ANUAL: {tma:.2f}')
print('Meses com temperatura acima da média: ')
for m in mon_med:
    print(m, end=' - ')