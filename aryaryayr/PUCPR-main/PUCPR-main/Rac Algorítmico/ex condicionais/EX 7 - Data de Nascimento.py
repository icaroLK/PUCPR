# cabeçalho
print('—'*40)
print(f'{"Data de Nascimento":^40}')
print('—'*40)
# coletando info
day = int(input('Que dia você nasceu? '))
mon = int(input('Qual mês? '))
year = int(input('E qual ano? '))
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mesabrv = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
mesnum = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

print('[1] Data simples')
print('[2] Data abreviada')
print('[3] Data completa')
ans = int(input('Como deseja visualizar a data? '))
print('~'*30)
#mostrando resultados
if ans == 1:
    print(f'Você nasceu dia {day}/{mon}/{year}')
if ans == 2:
    print(f'Você nasceu dia {day}/{mesabrv[mon-1]}/{year}')
if ans == 3:
    print(f'Você nasceu dia {day} de {mes[mon-1]} de {year}')