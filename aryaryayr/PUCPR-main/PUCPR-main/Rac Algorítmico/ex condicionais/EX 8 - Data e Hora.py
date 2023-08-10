# cabeçalho
print('—'*40)
print(f'{"Data e Hora":^40}')
print('—'*40)
# coletando info
day = int(input('Dia: '))
mon = int(input('Mês: '))
year = int(input('Ano: '))
hour = int(input('Hora: '))
min = int(input('Minuto: '))
sec = int(input('Segundo: '))
print('~'*40)
print(f'{day}/{mon}/{year} - {hour}:{min}:{sec}')

print('[1] Dias')
print('[2] Mêses')
print('[3] Anos')
print('[4] Horas')
print('[5] Minutos')
print('[6] Segundos')
alt = int(input('O que deseja mudar? '))
if alt == 1:
    qnt = int(input('Deseja adicionar quantos dias? '))
    day += qnt
elif alt == 2:
    qnt = int(input('Deseja adicionar quantos mêses? '))
    mon += qnt
elif alt == 3:
    qnt = int(input('Deseja adicionar quantos anos? '))
    year += qnt
elif alt == 4:
    qnt = int(input('Deseja adicionar quantas horas? '))
    hour += qnt
elif alt == 5:
    qnt = int(input('Deseja adicionar quantos minutos? '))
    min += qnt
elif alt == 6:
    qnt = int(input('Deseja adicionar quantos segundos? '))
    sec += qnt
#calculando e mostrando resultados
if sec >= 60:
    min += sec // 60
    sec = sec % 60
if min >= 60:
    hour += min // 60
    min = min % 60
if hour >= 24:
    day += hour // 24
    hour = hour % 24
if mon <= 7 and mon != 2:
    if mon % 2 == 1:
        if day > 31:
            mon += day // 31
            day = day % 31
    if mon % 2 == 0:
        if day > 30:
            mon += day // 30
            day = day % 30
elif mon > 7 and mon != 2:
    if mon % 2 == 1:
        if day > 30:
            mon += day // 30
            day = day % 30
    if mon % 2 == 0:
        if day > 31:
            mon += day // 31
            day = day % 31
elif mon == 2:
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        if day > 29:
            mon += day // 29
            day = day % 29
    else:
        if day > 28:
            mon += day // 28
            day = day % 28
if mon > 12:
    year += mon // 12
    mon = mon % 12

print(f'{day:02d}/{mon:02d}/{year:02d} - {hour:02d}:{min:02d}:{sec:02d}')
