dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
hora = int(input('Insira a hora (formato 24h): '))
min = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))

print('\nData atual: \n{:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(dia, mes, ano, hora, min, seg))

add = int(input('''\nSelecione a unidade de tempo que deseja adicionar:
[1] Dia
[2] Mes
[3] Ano
[4] Horas
[5] Minutos
[6] Segundos
R: '''))

qtd = int(input('Insira a quantidade de tempo que será adicionada: '))

if add == 6:
    seg += qtd
elif add == 5:
    min += qtd
elif add == 4:
    hora += qtd
elif add == 3:
    ano += qtd
elif add == 2:
    mes += qtd
else:
    dia += qtd






if seg >= 60:
    min += seg // 60
    seg = seg % 60
if min >= 60:
    hora += min // 60
    min = min % 60
if hora >= 24:
    dia += hora // 24
    hora = hora % 24


# aqui é pra deixar os meses certos com 30 e 31 dias e fevereiro com 28
if dia > 28 and mes == 2:   #add aqui o ano bissexto
    mes += dia // 28
    dia = dia % 28
elif dia > 31 and mes <= 7 and mes != 2 and mes % 2 != 0:
    mes += dia // 31
    dia = dia % 31
elif dia > 30 and mes <= 7 and mes != 2 and mes % 2 == 0:
    mes += dia // 30
    dia = dia % 30
elif dia > 30 and mes > 7 and mes != 2 and mes % 2 != 0:
    mes += dia // 30
    dia = dia % 30
elif dia > 31 and mes > 7 and mes != 2 and mes % 2 == 0:
    mes += dia // 31
    dia = dia % 31
# ate aqui


if mes > 12:
    ano += mes // 12
    mes = mes % 12
print('Nova data:\n{:02d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(dia, mes, ano, hora, min, seg))
